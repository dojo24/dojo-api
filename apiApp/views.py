from rest_framework import viewsets

from apiApp.serializers import *
from apiApp.models import *

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer


class SquishiesViewSet(viewsets.ModelViewSet):
    queryset = Squishies.objects.all()
    serializer_class = SquishiesSerializer
