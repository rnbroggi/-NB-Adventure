from django.urls import path
from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.JournalMainView.as_view(), name='journal'),
    path('creation/', views.new_post, name='create'),
    path('entries/', views.PostListView.as_view(), name='entries'),
    path('edit/<pk>/', views.PostEditView.as_view(), name='edit'),
    path('entries/<pk>', views.PostDetailView.as_view(), name='entry-detail'),
    path('delete/<pk>/', views.PostDeleteView.as_view(), name='delete'),
]
