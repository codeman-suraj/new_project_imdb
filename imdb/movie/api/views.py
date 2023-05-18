from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from movie.models import StreamPlatform, Movie
from . serializers import MovieSerializer, StreamPlatformSerializer

class Streamlist(APIView):
    
    def get(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Streamdetails(APIView):
    
    def get(self, request, pk):
        queryset = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        queryset = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        queryset = StreamPlatform.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
        
class Movielist(APIView):
    def get(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class Moviedetails(APIView):
    
    def get(self, request, pk):
        queryset = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        queryset = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        queryset = Movie.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        