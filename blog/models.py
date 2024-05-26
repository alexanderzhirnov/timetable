from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=256)
    short_description = models.TextField()
    description = models.TextField()
    slug = models.SlugField(max_length=512)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return self.title

class PageVisit(models.Model):
    page_id = models.IntegerField()
    session_id = models.UUIDField(null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Page ID: {self.page_id}, User ID: {self.user_id}, Date: {self.date}"