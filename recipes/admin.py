from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')  # Display these fields in the admin list view

admin.site.register(Recipe, RecipeAdmin)
