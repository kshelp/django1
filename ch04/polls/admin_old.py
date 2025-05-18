from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):  # 테이블 형식으로 보여주기
# class ChoiceInline(admin.StackedInline):  # Choice 모델 클래스 같이 보기
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # 필드 순서 변경
    fieldsets = [  # 각 필드 분리
        ('Question Statement', {'fields': ['question_text']}),
        # ('Date Information', {'fields': ['pub_date']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),  # 필드 접기
    ]
    inlines = [ChoiceInline]  # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date')  # 레코드 리스트 컬럼 지정

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
