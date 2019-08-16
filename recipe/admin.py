from django.contrib import admin
from .models import *


class RecipeList(admin.ModelAdmin):

    list_display = ('recipe_name', 'author')
    search_fields = ('recipe_name',)

admin.site.register(Recipe, RecipeList)