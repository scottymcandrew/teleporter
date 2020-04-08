from django.test import TestCase


class TestViews(TestCase):
    """
    Test Blog All Posts Views. This does not cover adding new blog posts because that is performed by
    site admins in Django Administration
    """
    def test_get_all_blog_posts(self):
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog/all_blog_posts.html")
