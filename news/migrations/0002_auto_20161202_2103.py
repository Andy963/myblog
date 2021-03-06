# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='catagory',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name', 'total_blog'], 'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='news.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='最近修改日期'),
        ),
    ]
