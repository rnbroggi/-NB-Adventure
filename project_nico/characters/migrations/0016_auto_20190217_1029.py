# Generated by Django 2.1.7 on 2019-02-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0015_auto_20190217_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, default='None.jpg', upload_to=''),
        ),
    ]
