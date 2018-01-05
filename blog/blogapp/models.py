# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#For the usage of reverse function, making URL patterns
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)