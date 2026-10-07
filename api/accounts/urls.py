
from django.urls import path, include
from rest_framework import routers
from api.accounts import views
router = routers.DefaultRouter()

router.register("user-register", views.RegisterApiViewSet, basename='user-register')
router.register("user-signin", views.SignInApiViewSet, basename='user-signin')


urlpatterns = [

]+router.urls
