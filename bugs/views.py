from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bug, BugComment
from .forms import CreateBugReport, BugCommentForm


@login_required
def all_bugs(request):
    bugs = Bug.objects.all().order_by('user_votes', '-created')
    return render(request, 'bugs/bugs.html',
                  {'bugs': bugs})


@login_required
def bug_detail(request, id):
    bug = get_object_or_404(Bug, id=id)

    # Comments
    comments = bug.comments.all()

    new_comment = None

    if request.method == 'POST':
        # A new comment is being posted
        bug_comment_form = BugCommentForm(data=request.POST)
        if bug_comment_form.is_valid():
            # Comment object created but not saved to DB yet
            new_comment = bug_comment_form.save(commit=False)
            # Assign new comment to bug
            new_comment.bug = bug
            # Save to DB
            new_comment.save()
    else:
        # Get request return empty form
        bug_comment_form = BugCommentForm

    return render(request, 'bugs/bug/bug_detail.html',
                  {'bug': bug,
                   'comments': comments,
                   'new_comment': new_comment,
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
