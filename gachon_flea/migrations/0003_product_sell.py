# Generated by Django 3.1.1 on 2020-12-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gachon_flea', '0002_auto_20201215_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sell',
            field=models.BooleanField(default=False),
        ),
    ]
