# room/urls.py
from django.urls import path
from .views import Rooms, RoomView

urlpatterns = [
    path('', Rooms.as_view(), name='rooms'),
    path('<slug:slug>/', RoomView.as_view(), name='room'),
]
