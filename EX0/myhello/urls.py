# mysite/urls.py
from django.contrib import admin
from django.urls import path, include  # 記得要多 import 一個 include

urlpatterns = [
    path('admin/', admin.admin.site.urls),
    
    # 只要網址是 myhello/ 開頭的，都去讀取 myhello.urls 裡的設定
    path('myhello/', include('myhello.urls')),
]