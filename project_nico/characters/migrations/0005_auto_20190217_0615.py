# Generated by Django 2.1.7 on 2019-02-17 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20190217_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='char_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Class'),
        ),
    ]
