# Generated by Django 3.1.7 on 2021-02-25 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20210225_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe'),
        ),
    ]