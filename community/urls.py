from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LostFoundPetViewSet

router = DefaultRouter()
router.register(r'lost-found-pets', LostFoundPetViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]
