from django.urls import path
from . import views

app_name = 'rpg'

urlpatterns = [
    path('', views.RpgView.as_view(), name='rpg'),
    path('battle/<pk>', views.RpgBattleView.as_view(), name='battle'),
    path('instructions/', views.RpgInstructionsView.as_view(), name='instructions'),
]
