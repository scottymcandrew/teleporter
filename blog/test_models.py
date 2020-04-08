from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post, PostComment


class TestPostModel(TestCase):
    def test_created_defaults_to_now(self):
        user = User.objects.get(username='admin')
        post = Post(title='Create a test')
        post.save()
        self.assertEqual(post.created, datetime.now())
