from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
]