# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def surveys(request):
  response = "placeholder to display all the surveys created"

  return HttpResponse(response)

def new(request):

  return HttpResponse("placeholder for users to add a new survey")


# Create your views here.
