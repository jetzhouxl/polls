from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
# Create your views here.
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    #所谓的上下文环境就是传入模板里面的参数，一定要参数名对应
    context={
        #由变量名加对象组成的字典
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    response="you are looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse("you are voting on question %s." %question_id)