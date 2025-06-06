from django.contrib import admin
from polls.models import Question, Choice

# class ChoiceInline(admin.StackedInline): # Question 및 Choice를 한 화면에서 보기
class ChoiceInline(admin.TabularInline):  # 테이블 형식으로 보여주기
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # 필드 순서 변경
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        # ('Date Information', {'fields': ['pub_date']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # Question 및 Choice를 한 화면에서 보기
    list_display = ('question_text', 'pub_date')  # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date']  # 필터 사이드 바 추가
    search_fields = ['question_text']  # 검색 박스 추가

#admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
