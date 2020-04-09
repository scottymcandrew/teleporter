from django.test import TestCase
from datetime import datetime, date
from django.contrib.auth.models import User
from blog.models import Post, PostComment


class TestViews(TestCase):
    """
    Test Blog All Posts Views. This does not cover adding new blog posts because that is performed by
    site admins in Django Administration
    """

    def test_get_all_blog_posts(self):
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog/all_blog_posts.html")

    def test_get_blog_post_detail(self):
        user = User.objects.create_user(username='test', password='test123')
        post = Post.objects.create(title='test title', author=user, text='test body', slug='abc')
        url = post.get_absolute_url()
        page = self.client.get(url)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog/blog_post_detail.html")
