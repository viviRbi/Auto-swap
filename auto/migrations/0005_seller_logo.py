# Generated by Django 3.0.3 on 2020-02-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_auto_20200211_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='logo',
            field=models.URLField(default='', max_length=100),
        ),
    ]
