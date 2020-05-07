from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.contrib.auth.decorators import login_required
# Create your views here.
#merge comment

def index(response, id): #you are creating items of a list here

    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)
            if 'save' in response.POST:
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()
            elif 'delete' in response.POST:
                delete_item_id = response.POST['delete_item']
                print(delete_item_id,"item to delete")
                item_to_delete = Item.objects.get(id = delete_item_id)
                item_to_delete.delete()
            elif response.POST.get("newItem"):
                txt=response.POST.get("new")

                if len(txt) > 0:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})
    else:
        return render(response, "main/home.html", {})

def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        # print('ok')
        # print(response.POST)
        form = CreateNewList(response.POST)#this line over here. response.POST compulsory
        n = None
        if form.is_valid():
            n = form.cleaned_data["name"]
            s = ToDoList(name=n,user = response.user)
            s.save()
            #response.user.todolist.add(s)

        addr = "/" + str(s.id)
        return HttpResponseRedirect(addr)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

def all(response):
    all_list = ToDoList.objects.filter(user = response.user)
    return render(response,'main/all.html',{'complete_list':all_list})

def view(response):
    return render(response, 'main/view.html', {})
