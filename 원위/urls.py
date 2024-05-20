from django.urls import path

from 원위 import views

app_name = '원위'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
]