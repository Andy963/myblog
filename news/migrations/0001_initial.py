# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('content', models.TextField(max_length=10000, verbose_name='内容')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期')),
                ('update_date', models.DateTimeField(default=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期'), verbose_name='最近修改日期')),
                ('clickCount', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('comment', models.TextField(blank=True, max_length=200, null=True, verbose_name='评论')),
                ('isRecommend', models.BooleanField(default=False, verbose_name='推荐')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-pub_date', 'clickCount'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.IntegerField(blank=True, null=True, verbose_name='性别')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='生日')),
                ('registerTime', models.DateTimeField(blank=True, null=True, verbose_name='注册日期')),
                ('latestLogTime', models.DateTimeField(blank=True, null=True, verbose_name='最近登陆日期')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮件')),
                ('total_blog', models.IntegerField(default=0, verbose_name='文章总数')),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('index', models.IntegerField(default=999, verbose_name='分类排序')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author'),
        ),
    ]
