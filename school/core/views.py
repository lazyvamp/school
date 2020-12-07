from django.shortcuts import render
from django.http import JsonResponse
import json
from core.forms import UserSignUpForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        guest = UserSignUpForm(request_data)
        if guest.is_valid():
            guest.save()
            return JsonResponse({'message': 'User ssaved successfully...!!'})
        else:
            return JsonResponse({'message': 'Information is not valid', 'errors': guest.errors})
    else:
        return JsonResponse({'message': 'Page not found'})