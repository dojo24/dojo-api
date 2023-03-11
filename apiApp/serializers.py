from rest_framework import serializers
from apiApp.models import *

class CharactersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Characters
        fields = ('id', 'name', 'birthDay', 'spouse', 'voice', 'img')

class SquishiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Squishies
        fields = ('id', 'name', 'img')

class StickerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stickers
        fields = ('id', 'name', 'img', 'category')
