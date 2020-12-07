from django.shortcuts import render
from django.http import JsonResponse
import json
from core.forms import UserSignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from core.models import BaseUser
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def admin_register(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        guest = UserSignUpForm(request_data)
        if guest.is_valid():
            if request_data['role'] == 'admin':
                group = Group.objects.get(name='Admin')
            else:
                return JsonResponse({'message': 'User is not invited for admin'})
            user = guest.save()
            user.groups.add(group)
            return JsonResponse({'message': 'User ssaved successfully...!!'})
        else:
            return JsonResponse({'message': 'Information is not valid', 'errors': guest.errors})
    else:
        return JsonResponse({'message': 'Page not found'})


@login_required
@permission_required('can_add_student')
def student_register(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        request_data['role'] == 'student'
        guest = UserSignUpForm(request_data)
        if guest.is_valid():
            user = guest.save()
            user.groups.add(Group.objects.get(name='Student'))
            return JsonResponse({'message': 'Student Registered successfully...!!'})
        else:
            return JsonResponse({'message': 'invalid data', 'errors': guest.errors})
    else:
        return JsonResponse({'message': 'Page not found'})

@login_required
@permission_required('can_add_teacher')
def teacher_register(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        request_data['role'] == 'teacher'
        guest = UserSignUpForm(request_data)
        if guest.is_valid():
            user = guest.save()
            user.groups.add(Group.objects.get(name='Teacher'))
            return JsonResponse({'message': 'Teacher Registered successfully...!!'})
        else:
            return JsonResponse({'message': 'invalid data', 'errors': guest.errors})
    else:
        return JsonResponse({'message': 'Page not found'})

@login_required
def user_login(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        guest = authenticate(request, username=request_data['username'], password=request_data['password'])
        if guest is not None:
            login(request, guest)
            return JsonResponse({'message': 'Login done..!!'})
        else:
            return JsonResponse({'message': 'Invalid username or password'})
    else:
        return JsonResponse({'message': 'Page not found'})

@login_required
def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'user Logged out successfully...!!'})

#Dashboard API's
@login_required
def admin_dash(request):
    if request.method == "GET" and request.user.role == 'admin':
        list_users = BaseUser.objects.all()
        admin_info = {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'phone_number': request.user.phone_number
        }
        return JsonResponse({'message': 'List of all Users', 'list': list_users, 'self_info': admin_info})
    else:
        return JsonResponse({'message': 'Page not found'})

@login_required
def student_dash(request):
    if request.method == "GET":
        try:    
            my_user = request.user
            information = {
                'username': my_user.username,
                'first_name': my_user.first_name,
                'last_name': my_user.last_name,
                'email': my_user.email,
                'phone_number': my_user.phone_number
            }
            return JsonResponse({'message': 'data found', 'info': information})
        except BaseUser.DoesNotExist:
            return JsonResponse({'message': 'Requested Student data does not exist in database'})
    else:
        return JsonResponse({'message': 'Page not found'})

@login_required
def teacher_dash(request):
    if request.method == "GET" and request.user.role in BaseUser.FACULTY_ROLES:
        try:
            teacher = request.user
            information = {
                'username': teacher.username,
                'first_name': teacher.first_name,
                'last_name': teacher.last_name,
                'email': teacher.email,
                'phone_number': teacher.phone_number
            }
            return JsonResponse({'message': 'data found', 'info': information})
        except BaseUser.DoesNotExist:
            return JsonResponse({'message': 'Information of requested teacher is not found in database..!!'})
            
