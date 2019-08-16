from django.db import models
from django.contrib.auth import get_user_model


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50, null=False, unique=True, blank=False)
    author = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.recipe_name


class Step(models.Model):
    step = models.TextField(max_length=300)
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)

    def __str__(self):
        return self.step


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient

