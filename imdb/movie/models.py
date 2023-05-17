from django.db import models

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    review = models.IntegerField()
    platform = models.ForeignKey(StreamPlatform, null=False, blank=False, on_delete=models.CASCADE, related_name="platform")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    