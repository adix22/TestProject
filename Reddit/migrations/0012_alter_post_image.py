# Generated by Django 4.0.4 on 2022-05-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
