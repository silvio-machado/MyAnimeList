# Generated by Django 2.0 on 2018-02-27 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animes',
            name='style',
        ),
    ]
