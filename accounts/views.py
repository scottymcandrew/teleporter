from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


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


@login_required
def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html',
                  {'section': user_dashboard})
