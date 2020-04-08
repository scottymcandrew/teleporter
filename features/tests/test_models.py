from datetime import date
from django.contrib.auth.models import User
from django.test import TestCase
from features.models import Feature, FeatureComment


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test123')
        test_feature_main = Feature.objects.create(title='test title', author=cls.user, description='test body')
        FeatureComment.objects.create(feature=test_feature_main, author=cls.user, comment='test comment')

    def test_create_feature_and_check_created_is_today(self):
        feature = Feature.objects.get(id=1)
        self.assertEqual(feature.created.date(), date.today())

    def test_create_post_comment(self):
        feature_comment = FeatureComment.objects.get(id=1)
        self.assertEqual(feature_comment.created.date(), date.today())