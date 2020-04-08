from datetime import datetime, date
from django.contrib.auth.models import User
from django.test import TestCase
from bugs.models import Bug, BugComment


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test123')
        test_bug_main = Bug.objects.create(title='test title', author=cls.user, description='test body')
        BugComment.objects.create(bug=test_bug_main, author=cls.user, comment='test comment')

    def test_create_bug_and_check_created_is_today(self):
        bug = Bug.objects.get(id=1)
        self.assertEqual(bug.created.date(), date.today())

    def test_create_post_comment(self):
        bug_comment = BugComment.objects.get(id=1)
        self.assertEqual(bug_comment.created.date(), date.today())
