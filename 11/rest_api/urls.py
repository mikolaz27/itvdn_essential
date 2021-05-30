from django.urls import include, path
from rest_framework import routers
from .views import CarViewSet, ModelViewSet, MakeViewSet

router = routers.DefaultRouter()
router.register(r'make', MakeViewSet, basename='make')
router.register(r'model', ModelViewSet, basename='model')
router.register(r'car', CarViewSet)

urlpatterns = [
    path('', include((router.urls, 'rest_api'), namespace='rest_api')),
]
