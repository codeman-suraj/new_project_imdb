from rest_framework import serializers
from movie.models import StreamPlatform, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    platform = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
