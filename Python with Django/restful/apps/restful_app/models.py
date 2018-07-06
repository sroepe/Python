# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    if len(postData["first_name"]) < 3:
      errors["name"] = "First name should be more than 3 characters."
    if len(postData["last_name"]) < 3:
      errors["name"] = "First name should be more than 3 characters."
    return errors

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

# Create your models here.
