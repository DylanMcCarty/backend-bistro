from django.shortcuts import render
from .models import MenuItems, Category, Cuisine
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def getMenu(request):
    data = [i.json() for i in MenuItems.objects.all()]
    return HttpResponse(json.dumps(data), content_type='application/json')
