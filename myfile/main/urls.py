from django.urls import path
from . import views
from accounts import views as vs

urlpatterns = [
    path("<int:id>", views.index, name='index'),
    path("", vs.login, name="login"),
    path("create/", views.create, name="create"),
    path('all/', views.all, name="all"),
    path('home/', views.home, name="homeg"),
    path('view/', views.view, name="view"),
]