# Generated by Django 4.1.6 on 2023-02-14 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_remove_question_answere_remove_question_op1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='answere',
            new_name='answer',
        ),
    ]
