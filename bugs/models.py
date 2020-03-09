from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Bug(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bugs_reported', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    user_votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bugs_voted', blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Bug, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
