from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    """
    Model representing a blog post
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_posts',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='created')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('blog_post_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])

    def __str__(self):
        return self.title
