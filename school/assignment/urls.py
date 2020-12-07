from django.urls import path
from assignment import views

urlpatterns = [
    path('work', views.work , name='index' ),
]