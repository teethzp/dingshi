# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class Salts(models.Model):
	content=models.CharField(max_length=100)
