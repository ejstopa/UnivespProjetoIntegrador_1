# Generated by Django 3.2.7 on 2021-10-10 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attempt',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='attempt',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='theme_id',
            new_name='theme',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='user_id',
            new_name='user',
        ),
    ]
