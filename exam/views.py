from django.shortcuts import render
from . models import Subject,Question,Option,Submission
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as dlogin , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    subjects = Subject.objects.all()
    params = {'subjects': subjects}
    return render(request,'home.html',params)

fun1 = None
scoref = None
def quiz(request,id):      
    questions = Question.objects.filter(subject=id)
    options = Option.objects.filter(question__subject__subid = id)
    result = False
    score = -1
    if request.method == 'POST':

        result = True
        score = 0
        wrongans = []
        wrongques = []
        allanswer = []
        notfilled = []
        for question in questions:
            pname = "flexRadioDefault" + str(question.quesid)
            answer = request.POST.get(pname)
            if answer == None:
                notfilled.append(int (question.quesid))
            

            objt = Option.objects.filter(opid= answer)
            for obj in objt:
                allanswer.append(obj.opid)

                if obj.is_correct == True:
                    score = score+1
                else:
                
                    wrongans.append(int(answer)) 
                    wrongques.append(int (question.quesid)) 
                   
        student = request.user
        submission = Submission(user = student ,score = score) 
        submission.save()
        global fun1
        def fun1():
            return allanswer
        global scoref
        def scoref():
            return score
        params = {'questions': questions,'options':options,'result':result,'score':score,'wrongans':wrongans,'wrongques': wrongques,'subid':id, 'notfilled':notfilled }        
        return render(request,'quiz.html',params)

    params = {'questions': questions,'options':options,'result':result,'score':score}
    return render(request,'quiz.html',params)


@login_required
def submissions(request):
    results = Submission.objects.filter(user = request.user)
    params = {'result': results}
    return render(request,'submission.html',params)

def result(request,id):      
    questions = Question.objects.filter(subject=id)
    options = Option.objects.filter(question__subject__subid = id) 
    allanswer = fun1()
    score = scoref()
    # print(allanswer)
    params = {'questions': questions,'options':options , 'allanswer':allanswer,'score':score,'id':id}
    return render(request,'result.html',params)   
