# Generated by Django 3.1 on 2020-09-01 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
    ]
