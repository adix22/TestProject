# Generated by Django 4.0.4 on 2022-05-12 18:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subreddit',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed', 'You can use letters only')]),
        ),
    ]