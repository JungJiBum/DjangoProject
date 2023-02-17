# 별도의 생성이 필요한 urls.py
# app 폴더에 생성

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('crawling', views.crawling),
    path('delete/<str:idx>', views.deleteData),
    path('view/<str:idx>', views.viewData),

]
