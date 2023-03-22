from django.shortcuts import HttpResponse,render,redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect

def home(request):

    return render(request,'HomePage.html')
