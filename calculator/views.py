from django.http import HttpResponse
from django.shortcuts import render

from calculator.models import return_servings, call_recipe

DATA = {
    'omlet':["Омлет", {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    } ],
    'pasta': ["Паста",{
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    }],
    'buter': ["Бутерброд",{
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }],
    'hotdog': ["Хот-Дог",{
        'булка': 1,
        'сосиска': 1,
        'майонез, гр': 5,
        'кетчуп, гр': 5,
    }]
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def index(request):
    context = {
        'site':{}
    }
    for key, val in DATA.items():
        context['site'][key] = val[0]
    return render(request, "calculator/index.html", context)

def recipe(request, str1):
    servings = int(request.GET.get('servings',1))
    data_recipe_return = DATA[str1][1]
    recip_dish = call_recipe(data_recipe_return,servings)
    context = {
    }
    if str1 == 'omlet':
        context = {
            'dish': 'Омлет',
            'recipe': recip_dish,
            'servings': servings
        }
    elif str1 == 'buter':
        context = {
            'dish': 'Бутер',
            'recipe': recip_dish,
            'servings': servings
        }
    elif str1 == 'pasta':
        context = {
            'dish': 'Макароны',
            'recipe': recip_dish,
            'servings': servings
        }
    elif str1 == 'hotdog':
        context = {
            'dish': 'Хот-дог',
            'recipe': recip_dish,
            'servings': servings
        }
    else:
        context = {
            'dish': 'Какое-то неизвестное блюдо?!',
            'servings': servings
        }
    return render(request, "calculator/recipe.html",context)