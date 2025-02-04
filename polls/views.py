from django.shortcuts import render , get_object_or_404
from .models import Question , Choice
# Create your views here.
from django.http import HttpResponse, Http404 , HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic


# 메인 페이지 (index)
def index(request):
    # 1
    # return HttpResponse("Hello,world!")

    # 2
    # last_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in last_question_list])
    # return HttpResponse(output)

    # 3
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 4
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html" , context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """마지막으로 게시된 5개의 질문을 반환합니다."""
        return Question.objects.order_by("-pub_date")[:5]




# 상세 페이지 (detail)
def detail(request, question_id):
    #1
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #   raise Http404("Question does not exist")    
    # return render(request, "polls/detail.html", {"question" :question} )

    #2    
    question = get_object_or_404(Question,pk=question_id)    
    return render(request, "polls/detail.html", {"question": question})


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"



# 결과 페이지 (results)
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"



# 투표 페이지 (vote)
def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):    
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 게시물 데이터를 성공적으로 처리 한 후에는 항상 HttpResponseRedirect 로  results 페이지로 이동하므로서
        # 사용자가 뒤로 버튼및 새로고침시 데이터가 두 번 게시되는 것을 방지합니다.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



# 설문조사 결과 페이지
def results(reqest, question_id):
    question =get_object_or_404(Question, pk=question_id)
    return render(reqest, "polls/results.html", {"question": question})