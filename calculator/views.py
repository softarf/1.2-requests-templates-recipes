from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных persons
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def index_home(request):
    page_header = "<h1>Главная</h1>"
    dish_names = "<h3>Доступные блюда:</h3>"
    dish_list = ('&nbsp;' * 4) + ('<br>' + ('&nbsp;' * 4)).join([key for key in DATA.keys()])
    paragraph = "<p>Для получения количества необходимых инградиентов введите</p>"
    paragraph += "<p>в адресной строке браузера название блюда и количество порций:</p>"
    paragraph += "<p>а) в виде параметров представления, например 'calculate/omlet/4/';</p>"
    paragraph += "<p>б) в виде параметров строки запроса, например 'calculate/?dish=omlet&serv=4';</p>"
    paragraph += "<p>в) или в смешанном виде, например 'calculate/omlet/?serv=4'.</p>"
    paragraph += "<p>Для подсчёта на одну порцию, параметр 'serv' можно опустить.</p>"
    quote = page_header + dish_names + dish_list + paragraph
    return HttpResponse(quote)


def products_calculator(request, v_dish='None', v_serv=0):
    dish_name = request.GET.get("dish")
    servings = int(request.GET.get("serv", 1))
    if v_dish != 'None':
        dish_name = v_dish
        if v_serv != 0:
            servings = v_serv
    print(dish_name)
    recipe = None
    if DATA.get(dish_name) is not None:
        recipe = {}
        for ingredient, amount in DATA[dish_name].items():
            recipe[ingredient] = amount * servings
    context = {
        'dish_name': dish_name,
        'servings': servings,
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)
