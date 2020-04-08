from django.test import TestCase, Client
from django.contrib.auth.models import User
from features.models import Feature
from features.forms import CreateFeatureReport, FeatureCommentForm


class TestFeatureCommentForm(TestCase):
    """
    Test that we can create a new Feature Comment Form
    """
    c = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test123')
        # Log into the site to enable viewing of the feature app
        cls.c.login(username='test', password='test123')

    def test_create_feature_form(self):
        form = CreateFeatureReport({'title': 'test title',
                                    'description': 'test body',
                                    'author': self.user,
                                    'status': 'Requested',
                                    'category': 'User-Requested'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_field(self):
        form = CreateFeatureReport({'title': 'test title',
                                    'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])

    def test_can_create_a_comment(self):
        form = FeatureCommentForm({'comment': 'My comment'})
        self.assertTrue(form.is_valid())
