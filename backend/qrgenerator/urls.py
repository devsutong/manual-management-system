from django.urls import include, path
from qrgenerator import views
from rest_framework import  routers


urlpatterns = [
    path("post", view=views.ItemApiView.as_view()),
    path("qr/", views.qrgen_view),
    path("home/", views.Home.as_view()),
    path("items/", views.item_detail, name ="item_detail"),
    path('search/', views.search, name='search')
]