# Generated by Django 2.1.7 on 2019-02-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_auto_20190217_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, default='static/human.jpg', upload_to=''),
        ),
    ]
