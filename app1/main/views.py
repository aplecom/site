from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title':'Главная',
        'content':'Аренда селькохозяйственных комбайнов',
        'categories': categories
    }
    return render(request,'main/index.html',context)

def about(request):
    context = {
        'title':'Главная - о нас',
        'content':'О нас',
        'text_on_page':'Мы супер кАмпания и супер кОмпания!',
    }
    return render(request,'main/about.html',context)