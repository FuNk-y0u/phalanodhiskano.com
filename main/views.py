from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import ToDoList, Item
from . forms import CreateList
    # ! differnet views of main app !


##### ! home page !
def index(response):
    return render(response, "main/home.html", {})

##### ! id page !
def id(response, id):
    # ! finding the specific list from db !
    try:
        tlist = ToDoList.objects.get(id=id)
        id_page_dict = {"tlist":tlist, "id":id}
        return render(response, "main/list.html", id_page_dict)

    # ! error checking !
    except Exception as e:
        return HttpResponse('<h1> List Doesnot Exist </h1> </br> <h2> or something went wrong! </h2> </br> <h3 style="color:red"> ERR: </h3> <h4 style="color: red"> %s </h4>' %e)

##### ! error checking page!
def id_def(response):
    return HttpResponse("<h1> Oops! Please Write Correct Url! </h1>")

##### ! create page !
def create(response):
    form = CreateList()
    create_page_dict = {"form":form}
    if response.method == "POST":
        form = CreateList(response.POST)
        
        if form.is_valid():
            recv_name = form.cleaned_data["name"]
            recv_by_name = form.cleaned_data["by_name"]
            recv_tlist = ToDoList(name=recv_name,by_name=recv_by_name)
            recv_tlist.save()

        return HttpResponseRedirect("/id/%i" % recv_tlist.id)

    else:
        pass
    return render(response, "main/create.html",create_page_dict)
