# Generated by Django 4.0.4 on 2022-05-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0008_remove_post_id_alter_post_random_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='files/'),
        ),
    ]