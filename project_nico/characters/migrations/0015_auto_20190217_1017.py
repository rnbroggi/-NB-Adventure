# Generated by Django 2.1.7 on 2019-02-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0014_auto_20190217_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(blank=True, default='<django.db.models.fields.related.ForeignKey>.jpg', upload_to=''),
        ),
    ]
