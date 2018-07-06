# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  desc = models.TextField(null=True)
  

class Ninja(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  Dojo = models.ForeignKey(Dojo, related_name="Ninjas", null=True)



# Create your models here.
