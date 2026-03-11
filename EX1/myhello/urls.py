from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyHelloAPIView.as_view(), name='hello_api'),
]