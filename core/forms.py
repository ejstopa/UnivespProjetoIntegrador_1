from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Question, Theme, Attempt

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name, email, message)
        send_mail(
            'Contato Projeto Anki-Univesp', message, settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]       
        )

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['description', 'answer', 'theme', 'user']

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['description','user']