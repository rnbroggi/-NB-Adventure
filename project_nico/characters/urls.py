from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('creation/', views.CreateCharacterView.as_view(), name='create'),
    path('list/', views.CharactersListView.as_view(), name='list'),
    path('edit/<pk>/', views.CharacterEditView.as_view(), name='edit'),
    path('delete/<pk>/', views.CharacterDeleteView.as_view(), name='delete'),
]
