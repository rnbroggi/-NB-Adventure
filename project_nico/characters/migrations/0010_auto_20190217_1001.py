# Generated by Django 2.1.7 on 2019-02-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_auto_20190217_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, default='project_nico/static/project_nico/images/human.jpg', upload_to=''),
        ),
    ]
