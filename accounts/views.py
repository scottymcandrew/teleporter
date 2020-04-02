from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from features.models import Feature
from bugs.models import Bug
from .models import Profile
from django.contrib import messages


def authenticate_user(request):
    """
    View to authenticate a user with our LoginForm class
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # If validated, attribute cleaned_data is populated with the form data
            form_cleaned = form.cleaned_data
            user = authenticate(request, username=form_cleaned['username'], password=form_cleaned['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('You have authenticated successfully!')
                else:
                    return HttpResponse('This accounts is disabled')
            else:
                return HttpResponse('Invalid credentials')

    # If request is GET, return empty form
    else:
        form = LoginForm()
    # Load login template
    return render(request, 'registration/login.html',
                  {'form': form})


def register(request):
    """
    Allow new user registrations
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # We're not saving the new user object straight away
            new_user = user_form.save(commit=False)
            # Set password method of user model takes care of encryption
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Create an associated profile for the new user
            Profile.objects.create(user=new_user)
            return render(request, 'accounts/register_done.html',
                          {'new_user': new_user})
    else:
        # Empty form if GET request
        user_form = UserRegistrationForm()

    return render(request, 'accounts/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    """
    Allow users to edit their details and profile
    """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '  Profile has been updated successfully. Awesome!')
        else:
            messages.error(request, '  Uh oh, something went wrong updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'accounts/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def user_dashboard(request):
    my_voted_bugs = Bug.objects.all().select_related().filter(votes=request.user).order_by('-created')[:5]
    return render(request, 'accounts/user_dashboard.html',
                  {'section': user_dashboard,
                   'my_voted_bugs': my_voted_bugs})


def my_features_chart(request):
    """
    Features that the calling user have contributed to, for use in chart.js
    """
    labels = []
    data = []

    # Return all features where the calling user has contributed (paid!)
    queryset = Feature.objects.all().select_related().filter(funders=request.user).values()
    for entry in queryset:
        labels.append(entry['title'])
        data.append(entry['purchases'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

