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
    # Future use: adding images to posts
    photo = models.ImageField(upload_to='blog/%Y/', blank=True)

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


class PostComment(models.Model):
    """
    Allow comments for blog posts
    """
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='blog_comments')
    # Not a foreign key for this one to allow non-logged in users to submit comments (which need to be approved)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Set to active=true in development. In production this will be false and comments will be moderated.
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
