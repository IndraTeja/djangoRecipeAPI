from django.db import models
from django.contrib.auth.models import User
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50, null=False, unique=True, blank=False, primary_key=True)
    author = models.ForeignKey(User(), on_delete=models.CASCADE, blank=False)

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

