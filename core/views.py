from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm , QuestionForm, ThemeForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView, DetailView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Question, Theme, Attempt

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'
index = IndexView.as_view()

@login_required
def contact(request):
    success = False        
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

def help(request):
    return render(request, 'help.html')

def file(request):
    return render(request, 'file.html')

def project(request):
    return render(request, 'project.html')

##Classe para acesso as informações da tabela Theme
# class ThemeListView(ListView):
#     model = Theme

# class ThemeDetailView(DetailView):
#     model = Theme

def list_theme(request):
    themes = Theme.objects.all()
    user  = request.user
    user_id = user.id
    current_user= User.objects.get(id=user_id)
    user_themes = current_user.theme_set.all()
    return render(request, 'themes.html', {'themes': user_themes})


def create_theme(request):
    form = ThemeForm(request.POST or None)
    user  = request.user
    user_id = user.id
    form.initial["user"] = user_id
    if form.is_valid():
        form.initial["user"] = user_id
        form.save()
        return redirect('list_theme')

    return render(request, 'themes-form.html', {'form': form})


def update_theme(request, id):
    theme = Theme.objects.get(id=id)
    form = ThemeForm(request.POST or None, instance=theme)
    user  = request.user
    user_id = user.id
    form.initial["user"] = user_id
    if form.is_valid():
        form.initial["user"] = user_id
        form.save()
        return redirect('list_theme')

    return render(request, 'themes-form.html', {'form': form, 'theme': theme})


def delete_theme(request, id):
    theme = Theme.objects.get(id=id)

    if request.method == 'POST':
        theme.delete()
        return redirect('list_theme')

    return render(request, 'theme-delete-confirm.html', {'theme': theme})


##Classe para acesso as informações da tabela Question
# class QuestionListView(ListView):
#     model = Question

# class QuestionDetailView(DetailView):
#     model = Question

def list_question(request):
    questions = Question.objects.all()
    user  = request.user
    user_id = user.id
    current_user= User.objects.get(id=user_id)
    user_questions = current_user.question_set.all()
    return render(request, 'questions.html', {'questions': user_questions})


def create_question(request):
    form = QuestionForm(request.POST or None)
    user  = request.user
    user_id = user.id
    form.initial["user"] = user_id
    if form.is_valid():
        form.initial["user"] = user_id
        form.save()
        return redirect('core:list_question')

    return render(request, 'questions-form.html', {'form': form})


def update_question(request, id):
    question = Question.objects.get(id=id)
    form = QuestionForm(request.POST or None, instance=question)
    user  = request.user
    user_id = user.id
    form.initial["user"] = user_id
    if form.is_valid():
        form.initial["user"] = user_id
        form.save()
        return redirect('core:list_question')

    return render(request, 'questions-form.html', {'form': form, 'question': question})


def delete_question(request, id):
    question = Question.objects.get(id=id)

    if request.method == 'POST':
        question.delete()
        return redirect('core:list_question')

    return render(request, 'question-delete-confirm.html', {'question': question})

##Classe para acesso as informações da tabela Attempt
class AttemptListView(ListView):
    model = Attempt

class AttemptDetailView(DetailView):
    model = Attempt




