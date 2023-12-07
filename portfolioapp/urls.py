from django.urls import path
from .views import home,submit

urlpatterns=[
    path('',home,name="home"),
    path('submit/',submit,name="submit"),
]