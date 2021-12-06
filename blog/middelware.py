from django.shortcuts import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin



class UnderConstruction:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request, *args, **kwargs):
        response = reverse("about")
        return response

    

