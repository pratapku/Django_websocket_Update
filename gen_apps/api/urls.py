from django.urls import path,include
from gen_apps.api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Message',views.UserViewSet,basename='post')


urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]