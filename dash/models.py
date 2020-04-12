# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dash(models.Model):
    country = models.CharField(max_length=200,null= True)
    total = models.IntegerField(null= True)
    active = models.IntegerField(null= True)
    recovered = models.IntegerField(null= True)
    deaths = models.IntegerField(null= True)
    active = models.IntegerField(null= True)
    serious = models.IntegerField(null= True)
    tot_test = models.IntegerField(null= True)
    def __str__(self):
       return self.country
