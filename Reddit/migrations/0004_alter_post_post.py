# Generated by Django 4.0.4 on 2022-05-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
