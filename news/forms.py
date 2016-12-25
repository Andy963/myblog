#!/usr/bin/env python
#coding:utf-8
#@Author:Andy

from django import forms
from .models import Article , Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment

		fields = ['author', 'article', 'content']

		widgets = {
            # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
            # 例如 user_name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">
			"""'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入昵称",
                'aria-describedby': "sizing-addon1",
            }),
			"""
            'content': forms.Textarea(attrs={'placeholder': '我来评两句~'}),
        }
