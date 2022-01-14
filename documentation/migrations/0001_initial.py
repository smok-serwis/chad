# Generated by Django 4.0.1 on 2022-01-14 19:20

import datetime
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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Project label')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='Project slug')),
                ('created_on', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created on')),
                ('website', models.TextField(null=True, verbose_name='URL to the website')),
                ('description', models.TextField(verbose_name='Project description')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=255)),
                ('importance', models.IntegerField(default=10)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentation.project')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mimetype', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('data', models.BinaryField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentation.item')),
            ],
        ),
    ]
