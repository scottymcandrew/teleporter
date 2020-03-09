from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateBugReport


@login_required
def create_bug_report(request):
    if request.method == 'POST':
        form = CreateBugReport(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_bug = form.save(commit=False)
            # assign current user to the bug
            new_bug.user = request.user
            new_bug.save()
            messages.success(request, 'Bug reported successfully to our team')
            # redirect to new created bug detail view
            return redirect(new_bug.get_absolute_url())
    else:
        form = CreateBugReport()

    return render(request, 'bugs/create_bug_report.html',
                  {'form': form})
