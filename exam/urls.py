from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.onlinecourse , name='onlinecourse'),
    path('quiz/<int:id>',views.quiz , name='quiz'),
    path('submissions/',views.submissions,name='submissions'),
    path('result/<int:id>/',views.result,name='result')
    
]


# path('course/<int:course_id>/submission/<int:submission_id>/result/', ...),