# Generated by Django 4.2.7 on 2023-11-20 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
