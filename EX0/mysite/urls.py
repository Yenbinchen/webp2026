from django.contrib import admin
from django.urls import path, include  # 這裡一定要補上 include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 加入這行，把所有以 myhello/ 開頭的網址都轉交給 myhello 這個 app
    path('myhello/', include('myhello.urls')),
]