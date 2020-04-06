from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


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
    return render(request, 'blog/blog_post_detail.html',
                  {'post': post})
