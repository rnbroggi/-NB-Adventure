# Generated by Django 2.1.7 on 2019-02-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0018_auto_20190218_2146'),
        ('journal', '0004_auto_20190219_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='character',
        ),
        migrations.AddField(
            model_name='post',
            name='character',
            field=models.ManyToManyField(to='characters.Character'),
        ),
    ]