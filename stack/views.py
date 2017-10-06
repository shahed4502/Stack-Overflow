from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from datetime import datetime

from .models import Question, Answer

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'stack/index.html', context)

def ask_question(request):
    print(request.POST['question'])
    Question.objects.create(question_text=request.POST['question'], pub_date=datetime.now())
    return HttpResponseRedirect(reverse('stack:index'))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'stack/detail.html', {'question': question})

def answer(request, question_id):
    print(request.POST['answer'])
    question = get_object_or_404(Question, pk=question_id)
    Answer.objects.create(question=question, answer_text=request.POST['answer'])
    return HttpResponseRedirect(reverse('stack:detail', args=(question.id,)))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    voted_answer = question.answer_set.get(pk=request.POST['vote'])
    voted_answer.votes += 1
    voted_answer.save()
    return HttpResponseRedirect(reverse('stack:detail', args=(question.id,)))
