# Generated by Django 2.2.2 on 2019-06-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='category_name',
            field=models.TextField(default='Laptop'),
        ),
    ]
