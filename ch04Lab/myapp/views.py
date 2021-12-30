from django.shortcuts import render

# Create your views here.
# views.py
from django.http import HttpResponse
from django.views.generic import View

# 클래스형 뷰
class MyView(View):
    def get(self, request):
        # 뷰 로직 작성
        return HttpResponse('result')
        