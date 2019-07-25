from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name = "post"),
    path('posting/', views.posting, name = "posting"),
    path('post/<int:post_id>/', views.detail, name = "detail"),
    path('create/', views.create, name = "create"),
    
    ]