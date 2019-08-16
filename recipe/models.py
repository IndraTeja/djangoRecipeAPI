from django.db import models
from django.contrib.auth import get_user_model


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50, null=False, unique=True, blank=False, primary_key=True)
    author = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.recipe_name, self.author)
