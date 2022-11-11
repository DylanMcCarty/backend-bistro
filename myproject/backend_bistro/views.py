from django.shortcuts import render
from .models import MenuItems, Category, Cuisine
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def getMenu(request):
    # in this line i.json_items is referencing an attribute of the object and the for loop is looping through the object to find that function in the class object and run only that 
    data = [i.json_items() for i in MenuItems.objects.all()]
    # in this json.dumps is returning the data returned in the json items function and returning it as a json string, json dumps recognizes 
    # the queryset as a dictionary and converst that directly to json, admittedly i couldn't find out what content_type was doing!!!
    return HttpResponse(json.dumps(data), content_type='application/json')
