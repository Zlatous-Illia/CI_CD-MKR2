from django.shortcuts import render, get_object_or_404
from .models import Recipe


def main(request):
    recipes = Recipe.objects.filter(year=2023)
    return render(request, 'recipes/main.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
