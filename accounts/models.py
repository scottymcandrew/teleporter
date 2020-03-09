from django.db import models
from django.conf import settings


class Profile(models.Model):
    # Extend the User model: https://docs.djangoproject.com/en/2.2/topics/auth/customizing/
    # One to one - associate profiles with users. Delete profile when user deleted.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    # Requires pip Pillow library
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)


def __str__(self):
    return 'Profile for user {}'.format(self.user.username)
