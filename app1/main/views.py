from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'Главная',
        'content':'Аренда селькохозяйственных комбайнов',
    }
    return render(request,'main/index.html',context)

def about(request):
    return HttpResponse("About page")