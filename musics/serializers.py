from rest_framework import serializers
from .models import Music, Artist, Comment


class Musicserializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)


class Artistserializer(serializers.ModelSerializer):
    musics = Musicserializer(source="music_set", many=True)
    musics_count = serializers.IntegerField(source="music_set.count")

    class Meta:
        model = Artist
        fields = ('id', 'name')


class ArtistDetailserializer(serializers.ModelSerializer):
    musics = Musicserializer(source='music_set', many=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'musics')


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id')
