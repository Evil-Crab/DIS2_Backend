# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('requirements', models.TextField(blank=True)),
                ('badge', models.ImageField(upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'', blank=True)),
                ('bio', models.TextField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=7)),
                ('sigil', models.ImageField(upload_to=b'', blank=True)),
                ('members', models.ManyToManyField(related_name='groups', to='dis2_backend.AppUser', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('requirements', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('sigil', models.ImageField(upload_to=b'', blank=True)),
                ('members', models.ManyToManyField(related_name='schools', to='dis2_backend.AppUser', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='reward',
            name='school',
            field=models.ForeignKey(related_name='rewards', to='dis2_backend.School'),
        ),
        migrations.AddField(
            model_name='group',
            name='school',
            field=models.ForeignKey(related_name='groups', to='dis2_backend.School'),
        ),
        migrations.AddField(
            model_name='event',
            name='school',
            field=models.ForeignKey(related_name='events', to='dis2_backend.School'),
        ),
        migrations.AddField(
            model_name='event',
            name='students',
            field=models.ManyToManyField(related_name='events', to='dis2_backend.AppUser'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='students',
            field=models.ManyToManyField(related_name='achievements', to='dis2_backend.AppUser', blank=True),
        ),
    ]
