
from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('home/', views.HomeViewSet.as_view(), name="account-home"),
    path('test/', views.TextViewSet.as_view(), name="account-test"),


]
