from django.test import TestCase, Client
from django.contrib.auth.models import User
from bugs.models import Bug


class TestViews(TestCase):
    """
    Test Bugs App
    """
    c = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test123')
        # Log into the site to enable viewing of the bug app
        cls.c.login(username='test', password='test123')
        test_bug_main = Bug.objects.create(title='test title', author=cls.user, description='test body')

    def test_show_all_bugs(self):
        page = self.c.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/bugs.html")

    def test_show_bug_detail(self):
        page = self.c.get("/bugs/detail/1/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/bug/bug_detail.html")

    def test_create_bug_report(self):
        test_bug = Bug.objects.create(title='test title 2', author=self.user, description='test body 2')
        bug_id = str(test_bug.id)
        page = self.c.get("/bugs/detail/" + bug_id + "/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs/bug/bug_detail.html")
