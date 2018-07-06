# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
  def validate(self, postData):
    errors = []
    if len(postData["name"]) < 5:
      errors.append("Name should be 5 or more characters")
    if len(postData["desc"]) < 15:
      errors.append("Description should be 15 or more characters")
    return errors

class Course(models.Model):
  name = models.CharField(max_length=255)
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = CourseManager()

# Create your models here.
