from django.shortcuts import render
from django.http import HttpResponse
from . models import ToDoList, Item

#differnet views of main app

def index(response):
    return HttpResponse("<h1>Phalano Dhiskano</h1>")

def id(response, id):
    try:
        tlist = ToDoList.objects.get(id=id)
        return HttpResponse("<h1> %s </h1>" %(tlist.name))
    except Exception as e:
        return HttpResponse('<h1> List Doesnot Exist </h1> </br> <h2> or something went wrong! </h2> </br> <h3 style="color:red"> ERR: </h3> <h4 style="color: red"> %s </h4>' %e)

def id_def(response):
    return HttpResponse("<h1> Oops! Please Write Correct Url! </h1>")
