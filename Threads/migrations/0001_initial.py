# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=2000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Threads.Thread'),
        ),
    ]
