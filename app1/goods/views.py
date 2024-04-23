from django.shortcuts import render

def catalog(request):
    context = {
        'title': 'Главная - Каталог',
        'goods': [
        {'image': 'deps/images/goods/zer_John_Deere_s670.jpg',
         'name': 'Зерноуборочный комбайн John Deere',
         'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
         'price': 150.00},

         {'image': 'deps/images/goods/zer_claas_mega_360.jpg',
         'name': 'Зерноуборочный комбайн CLAAS MEGA-360',
         'description': 'Набор из стола и двух стульев в минималистическом стиле.',
         'price': 93.00},

         {'image': 'deps/images/goods/zer_don_1500b.jpg',
         'name': 'Зерноуборочный комбайн Дон 1500Б',
         'description': 'Кровать двухспальная с надголовником и вообще очень ортопедичная.',
         'price': 670.00},

         {'image': 'deps/images/goods/zer_dominator_mega_204.jpg',
         'name': 'Зерноуборочный комбайн Claas Dominator mega 204',
         'description': 'Кухонный стол для обеда с встроенной раковиной и стульями.',
         'price': 365.00},

         {'image': 'deps/images/goods/zer_СК_5М_1.jpg',
         'name': 'Зерноуборочный комбайн СК-5М-1 Нива + Жатка ЖВН',
         'description': 'Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.',
         'price': 430.00},

         {'image': 'deps/images/goods/sv_wic_Amity.jpg',
         'name': 'Свеклоуборочный комбайн WIC Amity',
         'description': 'Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!',
         'price': 610.00},

         {'image': 'deps/images/goods/sv_euro_tiger_210.jpg',
         'name': 'Свеклоуборочный комбайн Ropa Euro Tiger 2010 г.в',
         'description': 'Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).',
         'price': 55.00},

         {'image': 'deps/images/goods/sv_Franz Kleine_SF_10_2008.jpg',
         'name': 'Свеклоуборочный комбайн Franz Kleine SF 10, 2008',
         'description': 'Диван, он же софа обыкновенная, ничего примечательного для описания.',
         'price': 190.00},

         {'image': 'deps/images/goods/sv_holmer_terra_dos5.jpg',
         'name': 'Свеклоуборочный комбайн Holmer Terra Dos 5',
         'description': 'Описание товара, про то какой он классный, но это стул, что тут сказать...',
         'price': 30.00},

         {'image': 'deps/images/goods/sv_holmer_t3.jpg',
         'name': 'Свеклоуборочный комбайн Holmer t3',
         'description': 'Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.',
         'price': 10.00},

         {'image': 'deps/images/goods/korm_pcm_1401.jpg',
         'name': 'Кормоуборочный комбайн РСМ-1401',
         'description': 'Дизайнерский цветок (возможно искусственный) для украшения интерьера.',
         'price': 15.00},

         {'image': 'deps/images/goods/korm_don_680.jpg',
         'name': 'Кормоуборочный комбайн Дон 680',
         'description': 'Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.',
         'price': 25.00},
        ],
    }
    return render(request, 'goods/catalog.html',context)


def product(request):
    return render(request, 'goods/product.html')