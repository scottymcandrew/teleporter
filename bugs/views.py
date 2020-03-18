from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from common.decorators import ajax_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bug, BugComment, Vote
from .forms import CreateBugReport, BugCommentForm, SearchForm


@login_required
def all_bugs(request):
    bug_list = Bug.objects.all().order_by('votes', '-created')
    paginator = Paginator(bug_list, 4)
    page = request.GET.get('page')
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an int, return the first page
        bugs = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page
        bugs = paginator.page(paginator.num_pages)
    return render(request, 'bugs/bugs.html',
                  {'bugs': bugs,
                   'page': page})


@login_required
def bug_detail(request, id):
    bug = get_object_or_404(Bug, id=id)

    # Comments
    comments = bug.comments.all()

    paginator = Paginator(comments, 5)
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
        bug_comment_form = BugCommentForm(data=request.POST)
        if bug_comment_form.is_valid():
            # Comment object created but not saved to DB yet
            new_comment = bug_comment_form.save(commit=False)
            # Assign new comment to bug
            new_comment.bug = bug
            new_comment.author = request.user
            # Save to DB
            new_comment.save()
            messages.success(request, 'Your comment has been published.')
            return redirect('bug_detail', id)
    else:
        # Get request return empty form
        bug_comment_form = BugCommentForm

    return render(request, 'bugs/bug/bug_detail.html',
                  {'bug': bug,
                   'comments': comments,
                   'new_comment': new_comment,
                   'page': page,
                   'bug_comment_form': bug_comment_form})


@login_required
def create_bug_report(request):
    if request.method == 'POST':
        form = CreateBugReport(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_bug = form.save(commit=False)
            # assign current user to the bug
            new_bug.author = request.user
            new_bug.save()
            messages.success(request, 'Bug reported successfully to our team')
            # redirect to new created bug detail view
            return redirect(new_bug.get_absolute_url())
    else:
        form = CreateBugReport()
        return render(request, 'bugs/create_bug_report.html', {'form': form})


@ajax_required
@login_required
@require_POST
def bug_vote(request):
    bug_id = request.POST.get('id')
    action = request.POST.get('action')
    if bug_id and action:
        try:
            bug = Bug.objects.get(id=bug_id)
            if action == 'vote':
                bug.votes.add(request.user)
            else:
                bug.votes.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ko'})


def bug_search(request):
    form = SearchForm
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Bug.objects.annotate(search=SearchVector('title', 'description')).filter(search=query)

    return render(request, 'bugs/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})


class BugEdit(SuccessMessageMixin, UpdateView):
    model = Bug
    fields = ['title', 'description', 'severity', 'status']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('all_bugs')
    success_message = "Awesome, you just updated %(title)!"


class BugDelete(SuccessMessageMixin, DeleteView):
    model = Bug
    success_url = reverse_lazy('all_bugs')
    success_message = "Oh well, looks like you really did delete %(title)!"
