from django.urls import path
from core import views

urlpatterns = [
    #register API's
    path('admin/register', views.admin_register, name='admin_register'),
    path('teacher/register', views.teacher_register, name='teacher_register'),
    path('student/register', views.student_register, name='student_register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('forgot/password', views.forgot_password, name='password_forgot'),

    #dash API's
    path('admin/dash', views.admin_dash, name='admin_dashboard'),
    path('student/dash', views.student_dash, name='student_dashboard'),
    path('teacher/dash', views.teacher_dash, name='teacher_dashboard'),

]