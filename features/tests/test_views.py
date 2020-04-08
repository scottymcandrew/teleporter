from django.test import TestCase, Client
from django.contrib.auth.models import User
from features.models import Feature


class TestViews(TestCase):
    """
    Test Features App
    """
    c = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test123')
        # Log into the site to enable viewing of the feature app
        cls.c.login(username='test', password='test123')
        test_feature_main = Feature.objects.create(title='test title', author=cls.user, description='test body')

    def test_show_all_features(self):
        page = self.c.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/features.html")

    def test_show_feature_detail(self):
        page = self.c.get("/features/detail/1/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature/feature_detail.html")

    def test_create_feature_report(self):
        test_feature = Feature.objects.create(title='test title 2', author=self.user, description='test body 2')
        feature_id = str(test_feature.id)
        page = self.c.get("/features/detail/" + feature_id + "/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features/feature/feature_detail.html")