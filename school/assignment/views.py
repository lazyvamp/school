from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def work(request):
    return JsonResponse({'message': 'Hello User ..!!'})
