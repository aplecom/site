from django.shortcuts import render
from goods.models import Products
from goods.utils import q_search



def catalog(request,category_slug = None):

    query = request.GET.get("q",None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods= q_search(query)
    else:
        goods = Products.objects.filter(category__slug= category_slug)

    context = {
        'title': 'Главная - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html',context)


def product(request,product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product':product
    }
    return render(request, 'goods/product.html',context=context)