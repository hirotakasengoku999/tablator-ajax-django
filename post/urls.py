from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('like/', views.like, name='like'),
    path('update_user_check/', views.update_user_check, name='update_user_check'),
    path('update_note/', views.update_note, name='update_note'),
]