from django.db import models
from accounts.models import User

# Create your models here.

class Theme(models.Model):
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'theme'
    
    def __str__(self):
        return self.description

class Question(models.Model):
    description = models.CharField(max_length=250, null=False)
    answer = models.CharField(max_length=500)
    image = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'questions'
    
    def __str__(self):
        return self.description

class Difficults_options(models.IntegerChoices):
    EASY = 1
    MEDIUM = 2
    DIFFICULT = 3 

class Attempt(models.Model):
    attempt_number = models.IntegerField(null=False)
    attempt_date = models.DateTimeField(auto_now_add=True)
    got_it_right = models.BooleanField
    difficult = models.IntegerField(choices=Difficults_options.choices)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'attempts'
    


