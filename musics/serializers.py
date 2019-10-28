from rest_framework import serializers
from .models import Music


class Musicserializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)
