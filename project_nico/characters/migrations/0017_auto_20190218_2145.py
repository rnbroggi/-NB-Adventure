# Generated by Django 2.1.7 on 2019-02-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0016_auto_20190217_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, default=0, upload_to=''),
        ),
    ]
