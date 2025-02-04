import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="질문 내용")
    pub_date = models.DateTimeField('게시 날짜')

    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="최근 게시 여부", # 관리자 페이지에서 한글 라벨 적용
    )
    # def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="관련 질문")
    choice_text = models.CharField(max_length=200, verbose_name="선택지 내용")
    votes = models.IntegerField(default=0, verbose_name="투표 수")

    def __str__(self):
        return self.choice_text
    