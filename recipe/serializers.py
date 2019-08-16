from rest_framework import serializers
from .models import *


class RecipeSerializer(serializers.ModelSerializer):
    steps = serializers.StringRelatedField(many=True)
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ('recipe_name', 'author', 'steps', 'ingredients')


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ("id", "step", 'recipe')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id", "ingredient", "recipe")
