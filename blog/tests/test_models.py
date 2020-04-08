from datetime import datetime, date
from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post, PostComment


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test123')
        Post.objects.create(title='test title', author=cls.user, text='test body')
        post = Post.objects.get(id=1)
        PostComment.objects.create(post=post, name='test name', email='test@example.com',
                                                  comment='test comment')

    def test_create_post_and_check_created_is_today(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.created.date(), date.today())

    def test_create_post_comment(self):
        post_comment = PostComment.objects.get(id=1)
        self.assertEqual(post_comment.created.date(), date.today())
