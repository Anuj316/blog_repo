from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published') #to show only published posts

from taggit.managers import TaggableManager
class Post(models.Model):
    STATUS_CHOICES=(('draft', 'DRAFT'), ('published', 'PUBLISHED'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=256, unique_for_date='publish')
    author=models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True) #whenever the post object got created automatically that time will be considered
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects=CustomManager()
    tags=TaggableManager()

    class Meta:
        ordering=('-publish',) #descending order #also single value tuple ends with comma

    def __str__(self): #overriding __str__ that will be called internally
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])
#model related to comments section
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=64)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'Commented by {} on {}'.format(self.name, self.post)
