from django.shortcuts import render, get_object_or_404
from recipes.models import Book, Author


def main(request):
    # Отримати всі рецепти за 2023 рік
    recipes = Recipe.objects.filter(year=2023)
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    # Отримати деталі певного рецепту за його id
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
