from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.handlesignup,name="handlesignup"),
    path('login/',views.handlelogin,name="handlelogin"),
    path('logout/',views.handlelogout,name="handlelogout"),
]


