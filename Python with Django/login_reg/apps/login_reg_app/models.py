# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')


class UserManager(models.Manager):
  def reg_validate(self, postData):
    results = {'status': True, 'errors':[], 'user': None}
    #errors = []
    #name fields at least 2 characters, not blank, only alpha characters
    if len(postData["first_name"]) < 2 or len(postData["last_name"]) < 2:
      results['errors'].append("First/Last name should be 2 or more characters.")
      results['status'] = False
    if not NAME_REGEX.match(postData["first_name"]) or not NAME_REGEX.match(postData["last_name"]):
      results['errors'].append("First/Last name is not in a valid name format.")
      results['status'] = False
    #email validation
    if len(postData["email"]) < 1:
      results['errors'].append("Email is required")
      results['status'] = False
    if not EMAIL_REGEX.match(postData["email"]):
      results['errors'].append("This is not a valid email format")
      results['status'] = False
    if len(self.filter(email=postData["email"])) > 0:
      results['errors'].append("This email address is already registered.")
      results['status'] = False
    #password and confirmation validation - at least 8 characters in length, pw and confirm match
    if len(postData["pw"]) < 8:
      results['errors'].append("Password should be at least 8 characters in length.")
      results['status'] = False
    if postData["pwconfirm"] != postData["pw"]:
      results['errors'].append("Password confirmation does not match the password you entered.")
      results['status'] = False
    if len(postData["pwconfirm"]) < 1:
      results['errors'].append("Password Confirmation is required")
      results['status'] = False

    
    else:
      results["user"] = self.create(first_name = postData["first_name"], last_name = postData["last_name"], email = postData["email"], pw = bcrypt.hashpw(postData["pw"].encode(), bcrypt.gensalt()))
      
    return results

  def log_validate(self, postData):
    results = {'status': True, 'errors':[], "user": None}
    users = self.filter(email=postData["email"])
    if len(users) < 1:
      results['status'] = False
      results['errors'].append("This password does not exist.")
    else:
      if bcrypt.checkpw(postData["pw"].encode(), users[0].pw.encode()):
        results["user"] = users[0]
      else: 
        results["status"] = False

    return results

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  pw = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()


# Create your models here.
