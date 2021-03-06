# Generated by Django 3.1.3 on 2020-12-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gachon_flea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slugField', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slugField', max_length=100),
        ),
    ]
