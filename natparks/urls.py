from django.urls import path

from . import views

urlpatterns = [
    path('', views.PicNatParks.as_view()),
    path('api/', views.ListNatParks.as_view(), name='api'),
    path('api/<int:pk>/', views.DetailNatParks.as_view()),
]