#!/usr/bin/env python
#coding:utf-8
#@Author:Andy

from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _
from .models import Article , Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment

		fields = ['author', 'content']
		widgets = {
			'content': Textarea(attrs={'cols': 120, 'rows': 10, 'placeholder': '我来评两句~'}),
		}

		labels = {
			'content': _('content'),
		}
		help_texts = {
			'content': _('Some useful help text.'),
		}
		error_messages = {
			'content': {
				'max_length': _("This content name is too long."),
			},
		}
