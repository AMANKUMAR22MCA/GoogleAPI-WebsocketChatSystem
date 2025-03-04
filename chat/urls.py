from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_selection, name='user_selection'),  # User selection page
    path('room/', views.chat_room, name='chat_room'),  # Chat page
]
