from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('detail/<int:pk>/', article_detail_page, name='detail'),

]
