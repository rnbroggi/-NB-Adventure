# Generated by Django 2.1.7 on 2019-02-19 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0018_auto_20190218_2146'),
        ('journal', '0005_auto_20190219_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='character',
        ),
        migrations.AddField(
            model_name='post',
            name='character',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Character'),
        ),
    ]
