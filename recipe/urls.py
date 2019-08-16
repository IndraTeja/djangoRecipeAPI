# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import RecipeViewSet, StepViewSet, IngredientViewSet

router = routers.DefaultRouter()
router.register('recipes',RecipeViewSet, 'recipes')
router.register('steps', StepViewSet, 'steps')
router.register('ingredients', IngredientViewSet, 'ingredients')


urlpatterns = [
    path('', include(router.urls))
]