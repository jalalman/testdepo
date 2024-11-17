from django.urls import path
from . import views

app_name = 'tvshowapp'

urlpatterns =[
    path('allshows',views.allshows,name='allshows'),
    path('logout', views.logout, name='logout')
]