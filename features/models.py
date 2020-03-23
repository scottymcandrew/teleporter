from django.db import models
from django.conf import settings
from django.urls import reverse


class Feature(models.Model):
    """
    Model to hold details of features requested
    """

    FEATURE_STATUS = [
        ('Requested', 'Requested'),
        ('Implementing', 'Implementing'),
        ('Testing', 'Testing'),
        ('Implemented', 'Implemented'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='features_reported', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='feature_votes', through='FeatureVote')
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(max_length=12, default='Requested')

    def get_absolute_url(self):
        return reverse('feature_detail', args=[self.id])

    def __str__(self):
        return self.title


class FeatureComment(models.Model):
    """
    Model to store comments made against individual features
    """
    # Many to one relationship: a feature can have many comments
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='comments')
    # Authenticated users can comment
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='features_commented', on_delete=models.CASCADE, blank=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.feature)


class FeatureVote(models.Model):
    """
    Separate Feature Vote class used as a through field on the M2M relationship
    """
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
