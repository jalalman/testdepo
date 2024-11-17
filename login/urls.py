from django.urls import path
from . import views

app_name ='login'

urlpatterns = [
    path('',views.login,name='login'),
    path('createUser',views.createUser,name='createUser'),
    path('showshome',views.showshome,name='showshome'),
    path('loginConfirm',views.loginConfirm)

    ]