from django.urls import include, path
from rest_framework import routers
from apiApp import views

router = routers.DefaultRouter()
router.register(r'characters', views.CharacterViewSet)
router.register(r'squishies', views.SquishiesViewSet)
router.register(r'stickers', views.StickerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]