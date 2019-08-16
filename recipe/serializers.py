from rest_framework import serializers
from .models import *


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    steps = serializers.StringRelatedField(many=True)
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        field = ('name', 'author', 'step', 'ingredients', 'url')


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        field = ("id", "step", 'recipe')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        field = ("id", "ingredient", "recipe")
