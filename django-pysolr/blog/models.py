from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    summary = models.CharField(max_length=200, blank=False, null=False)
    author = models.ForeignKey(get_user_model(), blank=True, null=True, related_name="blogs", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        permissions = [
            ('view_all_blogs', 'Can view all blogs'),
        ]

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title

