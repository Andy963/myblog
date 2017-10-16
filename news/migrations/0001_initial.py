# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-22 10:49
from __future__ import unicode_literals

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最近修改日期')),
                ('click_count', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('recommend', models.IntegerField(choices=[(0, 'not_recommend'), (1, 'recommend')], default=False, verbose_name='推荐')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=10, verbose_name='状态')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-pub_date', 'click_count'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='姓名')),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'unknown')], default=2, verbose_name='性别')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='生日')),
                ('register_time', models.DateTimeField(blank=True, null=True, verbose_name='注册日期')),
                ('latest_log_time', models.DateTimeField(blank=True, null=True, verbose_name='最近登陆日期')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮件')),
                ('total_blog', models.IntegerField(default=0, verbose_name='文章总数')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
                'ordering': ['name', 'total_blog'],
            },
        ),
        migrations.CreateModel(
            name='Category',
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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200, verbose_name='评论内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('count', models.IntegerField(default=0, verbose_name='评论次数')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Article', verbose_name='评论所属文章')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author', verbose_name='评论作者')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Comment', verbose_name='父级评论')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['-pub_date'],
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='news.Tag', verbose_name='标签'),
        ),
    ]
