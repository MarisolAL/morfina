from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('draw_cards/', views.draw_cards, name='draw_cards'),
]
