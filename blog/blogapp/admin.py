# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from blogapp.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)