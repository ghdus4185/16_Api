from django.shortcuts import render, get_object_or_404
from .models import Music
from rest_framework.decorators import api_view
from .serializers import Musicserializer
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = Musicserializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, id):
    music = get_object_or_404(Music, id=id)
    serializer = Musicserializer(music)
    return Response(serializer.data)
