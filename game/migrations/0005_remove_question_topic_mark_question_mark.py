# Generated by Django 4.2.7 on 2023-11-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_remove_question_answer_displayed_question_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='topic',
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.topic')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='mark',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='game.mark'),
            preserve_default=False,
        ),
    ]
