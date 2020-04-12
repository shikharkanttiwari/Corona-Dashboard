# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Dash
from django.shortcuts import render
# Create your views here.
def show(request):
    dash=Dash.objects
    sum,active,deaths,recovered=0,0,0,0
    for i in dash.all():
        sum += i.total
        recovered += i.recovered
        active += i.active
        deaths += i.deaths
    active_per = active/sum*100
    active_per = round(active_per,2)
    deaths_per=round((deaths/sum*100),2)
    print(deaths_per)
    recovered_per=round((recovered/sum*100),2)
    return render(request,'dash/index.html',{'dash':dash,'sum':sum,'recovered':recovered,'recovered_per':recovered_per,'active':active,'active_per':active_per,'deaths':deaths,'deaths_per':deaths_per})
