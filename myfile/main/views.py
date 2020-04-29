from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response, id): #you are creating items of a list here
    print(id)
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if 'save' in response.POST:
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt=response.POST.get("new")

            if len(txt) >2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")


    return render(response, "main/list.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        print('ok')
        print(response.POST)
        form = CreateNewList(response.POST)#this line over here. response.POST compulsory
        n = None
        if form.is_valid():
            print('ok valid')
            n = form.cleaned_data["name"]
            print(n)
            s = ToDoList(name= n)
            s.save()
        addr = "/"+ str(s.id)
        return HttpResponseRedirect(addr)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


