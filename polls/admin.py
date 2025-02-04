from django.contrib import admin
from .models import Question, Choice


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("질문 정보", {'fields': ['question_text']}),  
#         ("날짜 정보", {'fields': ['pub_date']}),          
#     ]

#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("질문 정보",               {'fields': ['question_text']}),  # 질문 내용을 입력하는 필드
        ("날짜 정보", {'fields': ['pub_date'], 'classes': ['collapse']}),  # 날짜 정보 입력 필드 (접을 수 있음)
    ]
    
    inlines = [ChoiceInline]  # 연결된 Choice 모델을 같은 페이지에서 함께 관리할 수 있도록 설정
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 관리자 페이지 목록에서 표시할 필드들 지정
    list_filter = ['pub_date']  # 필터 옵션을 추가하여 날짜 기준으로 질문을 필터링할 수 있도록 설정
    search_fields = ['question_text']  # 질문 내용을 검색할 수 있도록 설정


admin.site.register(Question, QuestionAdmin)






