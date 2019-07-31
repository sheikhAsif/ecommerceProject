__author__ = 'Asif Mohd Sheikh'


from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="blogHome")
]
