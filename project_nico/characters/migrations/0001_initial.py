# Generated by Django 2.1.7 on 2019-02-16 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('level', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='ClassPower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='power_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack', to='characters.ClassPower'),
        ),
        migrations.AddField(
            model_name='class',
            name='power_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heal', to='characters.ClassPower'),
        ),
        migrations.AddField(
            model_name='character',
            name='char_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Class'),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Race'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]