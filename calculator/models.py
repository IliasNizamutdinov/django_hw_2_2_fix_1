from django.db import models


# Create your models here.
def return_servings(request):
    servings = request.GET.get("servings")
    if servings == None:
        servings = 1
    else:
        servings = int(servings)
    return servings

def call_recipe(data_recipe, servings):
    data_return = dict(data_recipe)
    for key, val in data_return.items():
        data_return[key] = round(val * servings,2)
    return data_return

