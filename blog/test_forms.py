from django.test import TestCase
from .forms import PostCommentForm


class TestPostCommentForm(TestCase):
    """
    Test that we can create a new Post Comment Form
    """
    def test_can_create_a_comment(self):
        form = PostCommentForm({'name': 'Create Tests',
                                'email': 'test@example.com',
                                'comment': 'My comment'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_field(self):
        form = PostCommentForm({'name': '',
                                'email': 'test@example.com',
                                'comment': 'My comment'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
