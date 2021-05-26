from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieSerializer
from .models import Movie, User

# Create your views here.

class TestView(APIView):
    permission_classes = {IsAuthenticated}

    def get(self, req, *args, **kwargs):
        qs = Movie.objects.filter(owner = req.user.id)
        serializer = MovieSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, req, *args, **kwargs):
        serializer = MovieSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save(owner=req.user)
            return Response(serializer.data)
        return Response(status=400,data=serializer.errors)


class HomeView(APIView):

    def get(self, req, *args, **kwargs):
        qs = Movie.objects.all()
        serializer = MovieSerializer(qs, many=True)
        return Response(serializer.data)
