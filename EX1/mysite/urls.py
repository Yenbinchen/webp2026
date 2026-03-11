# 確保第一行不是網址！
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myhello/', include('myhello.urls')),
]