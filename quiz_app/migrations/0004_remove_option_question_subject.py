# Generated by Django 4.1.6 on 2023-02-14 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_rename_answere_option_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='question_subject',
        ),
    ]
