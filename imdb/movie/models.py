from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    platform = models.ForeignKey(StreamPlatform, null=False, blank=False, on_delete=models.CASCADE, related_name="platform")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name= 'movie_name')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " | "+ str(self.movie_name.name)