from django.db import models

# Create your models here.

class Character(models.Model) :
    name = models.CharField(max_length=20) #CharField()는 max_length 필수
    feature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) #데이터가 만들어질 때 자동으로 날짜, 시간 기록
    updated_at = models.DateTimeField(auto_now=True)    #데이터 수정 시 자동으로 날짜, 시간을 기록

    def __str__(self):  #클래스를 출력할 때 이 함수를 호출하여 문자화한다
        return f'이름 : {self.name}, 특징 : {self.feature}, 만든날짜 : {self.created_at}, 수정날짜 : {self.updated_at}'