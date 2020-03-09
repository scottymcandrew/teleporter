from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
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
    return render(request, 'accounts/user_dashboard.html',
                  {'section': user_dashboard})
