import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question
from django.urls import reverse


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        미래는 ‘최근(recent)’이 아니기 때문에 이는 분명히 잘못된 것이다.
        1일 넘어가면 미래이다.
        was_published_recently()의 출력이 False가 되는지 확인.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


def create_question(question_text, days):
    """
    주어진 `question_text`로 질문을 생성하고,
    현재 시간으로부터 `days`만큼의 날짜 차이를 적용하여 발행일(`pub_date`)을 설정합니다.
    (과거에 발행된 질문은 음수, 아직 발행되지 않은 질문은 양수로 설정)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


def test_no_questions(self):
    """
    질문이 없을 경우, 적절한 메시지가 표시되는지 확인합니다.
    """
    response = self.client.get(reverse("polls:index"))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available.")
    self.assertQuerySetEqual(response.context["latest_question_list"], [])



class QuestionIndexViewTests(TestCase):
    def test_past_question(self):
        """
        과거에 발행된 질문이 인덱스 페이지에 표시되는지 확인합니다.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )


    def test_future_question(self):
        """
        미래에 발행될 질문은 인덱스 페이지에 표시되지 않는지 확인합니다.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])


    def test_future_question_and_past_question(self):
        """
        과거와 미래의 질문이 모두 존재할 경우, 과거의 질문만 표시되는지 확인합니다.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )




    def test_two_past_questions(self):
        """
        인덱스 페이지가 여러 개의 질문을 표시할 수 있는지 확인합니다.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )    





