from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from common.decorators import ajax_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Feature, FeatureComment
from .forms import CreateFeatureReport, FeatureCommentForm, SearchForm


@login_required
def all_features(request):
    feature_list = Feature.objects.all().order_by('-created')
    paginator = Paginator(feature_list, 4)
    page = request.GET.get('page')
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an int, return the first page
        features = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page
        features = paginator.page(paginator.num_pages)
    return render(request, 'features/features.html',
                  {'features': features,
                   'page': page})


@login_required
def feature_detail(request, id):
    feature = get_object_or_404(Feature, id=id)

    # Comments
    comments = feature.comments.all()

    paginator = Paginator(comments, 4)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an int, return the first page
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page
        comments = paginator.page(paginator.num_pages)

    new_comment = None

    if request.method == 'POST':
        # A new comment is being posted
        feature_comment_form = FeatureCommentForm(data=request.POST)
        if feature_comment_form.is_valid():
            # Comment object created but not saved to DB yet
            new_comment = feature_comment_form.save(commit=False)
            # Assign new comment to feature
            new_comment.feature = feature
            new_comment.author = request.user
            # Save to DB
            new_comment.save()
            messages.success(request, 'Your comment has been published.')
            return redirect('feature_detail', id)
    else:
        # Get request return empty form
        feature_comment_form = FeatureCommentForm

    return render(request, 'features/feature/feature_detail.html',
                  {'feature': feature,
                   'comments': comments,
                   'new_comment': new_comment,
                   'page': page,
                   'feature_comment_form': feature_comment_form})


@login_required
def request_feature(request):
    if request.method == 'POST':
        form = CreateFeatureReport(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_feature = form.save(commit=False)
            # assign current user to the feature
            new_feature.author = request.user
            new_feature.save()
            messages.success(request, 'Feature reported successfully to our team')
            # redirect to new created feature detail view
            return redirect(new_feature.get_absolute_url())
    else:
        form = CreateFeatureReport()
        return render(request, 'features/request_feature.html', {'form': form})


@ajax_required
@login_required
@require_POST
def update_feature_status(request):
    """
    This function is to facilitate site owners to update feature status in addition to admin console
    """
    feature_id = request.POST.get('id')
    action = request.POST.get('action')
    if feature_id and action:
        try:
            feature = Feature.objects.get(id=feature_id)
            feature.status = action
            feature.save()
            return JsonResponse({'status': 'ok', 'feature_status': action})
        except:
            pass
    return JsonResponse({'status': 'ko'})


def feature_search(request):
    """
    Search for a feature by title or description
    """
    form = SearchForm
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Feature.objects.annotate(search=SearchVector('title', 'description')).filter(search=query)

    return render(request, 'features/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})


class FeatureEdit(SuccessMessageMixin, UpdateView):
    """
    Uses Django Edit Form to provie update facility for a feature
    """
    model = Feature
    fields = ['title', 'description']
    template_name_suffix = '_update_form'
    success_message = "Awesome, you just updated this request"

    def get_success_url(self):
        return reverse('feature_detail', kwargs={
            'id': self.object.id,
        })


class FeatureDelete(SuccessMessageMixin, DeleteView):
    """
    Uses Django Edit Form to provie update facility for a feature
    """
    model = Feature
    success_url = reverse_lazy('all_features')
    success_message = "Oh well, looks like you really did delete %(title)"
