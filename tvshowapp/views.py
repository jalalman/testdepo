from django.shortcuts import render ,redirect ,HttpResponse
from .models import *
# Create your views here.

def allshows(request):
    show_id = request.session['id']
    context={
        'user':User.objects.get(id=show_id)
    }
    return render (request,'shows.html',context)


def logout(request):

    request.session.flush()

    return redirect("login:login")