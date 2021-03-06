from django.db import models
from django.conf import settings
from django.urls import reverse


class UserRequestedManager(models.Manager):
    def get_queryset(self):
        return super(UserRequestedManager, self).get_queryset() \
            .filter(category='User-Requested')


class RoadmapManager(models.Manager):
    def get_queryset(self):
        return super(RoadmapManager, self).get_queryset() \
            .filter(category='Roadmap')


class Feature(models.Model):
    """
    Model to hold details of features requested
    """

    FEATURE_STATUS = [
        ('Requested', 'Requested'),
        ('Funded', 'Funded'),
        ('Implementing', 'Implementing'),
        ('Testing', 'Testing'),
        ('Implemented', 'Implemented'),
    ]

    FEATURE_CATEGORY = [
        ('User-Requested', 'User-Requested'),
        ('Roadmap', 'Roadmap')
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='features_reported', null=True,
                               on_delete=models.SET_NULL)
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(max_length=12, default='Requested', choices=FEATURE_STATUS)
    when_implemented = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=50.00)
    purchases = models.DecimalField(max_digits=1000, decimal_places=0, default=0)
    category = models.CharField(max_length=16, default='User-Requested', blank=True, choices=FEATURE_CATEGORY)
    funders = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='feature_funders', blank=True)

    objects = models.Manager()  # The default manager.
    user_requested = UserRequestedManager()  # Our custom manager to retrieve User-Requested features.
    roadmap = RoadmapManager()  # Our custom manager to retrieve Roadmap features.

    def get_absolute_url(self):
        return reverse('feature_detail', args=[self.id])

    def get_funds_raised(self):
        funds_raised = self.purchases * self.price
        return funds_raised

    def __str__(self):
        return self.title


class FeatureComment(models.Model):
    """
    Model to store comments made against individual features
    """
    # Many to one relationship: a feature can have many comments
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='comments')
    # Authenticated users can comment
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='features_commented', on_delete=models.CASCADE,
                               blank=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.feature)
