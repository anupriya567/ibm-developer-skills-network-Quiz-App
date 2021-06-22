from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=200)
    subid = models.AutoField(primary_key= True)
    description = models.TextField(max_length=200,blank=True)
    image = models.ImageField(upload_to='course/images', default="")
    
    def __str__(self):  
        return self.name
   

class Question(models.Model):
    quesid = models.AutoField(primary_key= True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    questext = models.TextField(max_length=5000)
    points = models.IntegerField(default=0)
    def __str__(self):  
        return "ques " + str(self.quesid)

class Option(models.Model):
    opid = models.AutoField(primary_key= True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    opttext = models.TextField(max_length=500,default="")
    is_correct = models.BooleanField(default=False)
    def __str__(self):  
        return "ques " + str(self.question.quesid) +" | " + str(self.opid)

class Submission(models.Model):
    id = models.AutoField(primary_key= True)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete = models.CASCADE,default=None)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username + str(self.score)
