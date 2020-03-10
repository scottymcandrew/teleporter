from django.db import models
from django.conf import settings
from django.urls import reverse


class Bug(models.Model):

    SEVERITY_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    ]

    BUG_STATUS = [
        ('OPEN', 'Open'),
        ('ACTIVE', 'Active'),
        ('TESTING', 'Testing'),
        ('RESOLVED', 'Resolved'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bugs_reported', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    severity = models.CharField(max_length=10, default='LOW')
    user_votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bugs_voted')
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    status = models.CharField(max_length=10, default='OPEN')

    def get_absolute_url(self):
        return reverse('bugs:detail', args=[self.id])

    def __str__(self):
        return self.title
