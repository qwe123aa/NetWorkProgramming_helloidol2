from django.shortcuts import render
from django.views.generic import ListView

from 원위.models import Character


# Create your views here.
class CharacterListView(ListView):
    model = Character
    #character_list = Character.objects.all() #DB에 Character 데이터를 다 가져오자
    #return render(request, '콩순이/character_list.html', context={'character_list:character_list})
    #모델 list.html에 모델 list_라는 키로 DB에서 가져온 데이터를 넣어서 render하자
