from django.shortcuts import render,HttpResponse
from django.template import loader
from .models import UserDeatils

#Create your views here.
def sayhello(request):
    return HttpResponse("DJANGO PROJECT EXECUTED")
def html_page(request):
    return render(request, 'index.html')

def members(request):
    myusers = UserDeatils.objects.all().values()
    template = loader.get_template("all_users.html")
    context = {
        "myusers": myusers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    myusers = UserDeatils.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "myusers": myusers,
    }
    return HttpResponse(template.render(context,request))


    
