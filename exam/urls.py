from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('quiz/<int:id>',views.quiz , name='quiz'),
    path('submissions/',views.submissions,name='submissions'),
    path('result/<int:id>/',views.result,name='result')
    
]


# path('course/<int:course_id>/submission/<int:submission_id>/result/', ...),