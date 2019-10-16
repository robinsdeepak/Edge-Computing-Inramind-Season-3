from django.urls import path
from . import views

app_name = 'invoice'
urlpatterns = [
    path('', views.IndexView, name='IndexView'),
    path('upload_image/', views.simple_upload, name='upload'),
]
