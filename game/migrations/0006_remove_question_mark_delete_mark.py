# Generated by Django 4.2.7 on 2023-11-21 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_remove_question_topic_mark_question_mark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='mark',
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]
