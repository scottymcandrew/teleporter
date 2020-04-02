from datetime import timedelta
from django.db import models
from django.conf import settings
from django.urls import reverse


class Bug(models.Model):
    """
    Model to hold details of bugs reported to the system
    """
    SEVERITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    BUG_STATUS = [
        ('Open', 'Open'),
        ('Active', 'Active'),
        ('Testing', 'Testing'),
        ('Resolved', 'Resolved'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bugs_reported', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    severity = models.CharField(max_length=10, default='Low')
    votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bug_votes', through='BugVote')
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(max_length=10, default='Open')
    when_resolved = models.DateTimeField(auto_now_add=False, null=True)

    def get_absolute_url(self):
        return reverse('bug_detail', args=[self.id])

    def get_vote_count(self):
        return self.votes.count()

    def get_time_to_resolution(self):
        time_difference = self.when_resolved - self.created
        # Convert to days
        time_difference_in_minutes = time_difference / timedelta(days=1)
        return round(time_difference_in_minutes, 2)

    def __str__(self):
        return self.title


class BugComment(models.Model):
    """
    Model to store comments made against individual bugs
    """
    # Many to one relationship: a bug can have many comments
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='comments')
    # Authenticated users can comment
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bugs_commented', on_delete=models.CASCADE, blank=True)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.bug)


class BugVote(models.Model):
    """
    Separate Bug Vote class used as a through field on the M2M relationship
    """
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
