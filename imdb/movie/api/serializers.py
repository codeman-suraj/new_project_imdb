from rest_framework import serializers
from movie.models import StreamPlatform, Movie, Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    movie_name = RatingSerializer(many=True, read_only = True)
    class Meta:
        model = Movie
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    platform = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
