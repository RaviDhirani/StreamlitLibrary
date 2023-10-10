from django.urls import path
from . import views


urlpatterns =[
    path("", views.home, name="home"),
    # path("todos/",views.todo,name="ToDos"),
    # path("objectives/",views.objectives,name="Objectives")
    path("dashboard1/",views.dashboard1,name="dashboard1")
]
