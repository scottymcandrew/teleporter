from django.test import TestCase, Client
from django.contrib.auth.models import User
from bugs.models import Bug
from bugs.forms import CreateBugReport, BugCommentForm


class TestBugCommentForm(TestCase):
    """
    Test that we can create a new Bug Comment Form
    """
    c = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test123')
        # Log into the site to enable viewing of the bug app
        cls.c.login(username='test', password='test123')

    def test_create_bug_form(self):
        form = CreateBugReport({'title': 'test title',
                                'description': 'test body',
                                'author': self.user,
                                'severity': 'Medium',
                                'status': 'Open'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_field(self):
        form = CreateBugReport({'title': 'test title',
                                'description': '',
                                'severity': 'Medium',
                                'status': 'Open'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])

    def test_can_create_a_comment(self):
        form = BugCommentForm({'comment': 'My comment'})
        self.assertTrue(form.is_valid())
