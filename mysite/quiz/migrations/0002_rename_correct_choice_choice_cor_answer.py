# Generated by Django 4.1.3 on 2023-03-28 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='correct_choice',
            new_name='cor_answer',
        ),
    ]
