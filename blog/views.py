from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Post, PostComment
from .forms import PostCommentForm


def all_blog_posts(request):
    """
    Return all blog posts to display list on main blog page
    """
    post_list = Post.objects.all().order_by('-created')
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an int, return the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/all_blog_posts.html',
                  {'posts': posts,
                   'page': page})


def blog_post_detail(request, year, month, day, post):
    """
    Return the full blog post
    """
    post = get_object_or_404(Post, slug=post, created__year=year, created__month=month, created__day=day)
    active_comments = post.blog_comments.filter(active=True)

    paginator = Paginator(active_comments, 4)
    page = request.GET.get('page')
    try:
        active_comments = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an int, return the first page
        active_comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page
        active_comments = paginator.page(paginator.num_pages)

    new_comment = None

    if request.method == 'POST':
        post_comment_form = PostCommentForm(data=request.POST)
        if post_comment_form.is_valid():
            new_comment = post_comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request,
                             'Your comment has been published. By the way, in production this comment will be moderated, so please be civil ;-)')
            return redirect(post)
    else:
        post_comment_form = PostCommentForm()

    return render(request, 'blog/blog_post_detail.html',
                  {'post': post,
                   'active_comments': active_comments,
                   'new_comment': new_comment,
                   'post_comment_form': post_comment_form,
                   'page': page})
