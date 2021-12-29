from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    # /api/product/
    path('', views.ProductListAPI.as_view()),
]