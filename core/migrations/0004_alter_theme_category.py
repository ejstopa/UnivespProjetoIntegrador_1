# Generated by Django 3.2.7 on 2022-06-18 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220515_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Categoria'),
        ),
    ]