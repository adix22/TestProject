# Generated by Django 4.0.4 on 2022-06-03 18:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Reddit', '0015_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.AddField(
            model_name='comment',
            name='temporary_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
