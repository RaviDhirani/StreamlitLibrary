from django.shortcuts import render, HttpResponse
from .models import ToDoItem, Objectives
# Create your views here.
def home(request):
    return render(request,"home.html")

# Start of Original Code ____________________________________________
# def todo(request):
#     items = ToDoItem.objects.all()
#     return render(request,"todo.html",{"todos": items})
#
# def objectives(request):
#     items =Objectives.objects.all()
#
#     return render(request,"objectives.html",{"objectives": items})
# End of Original Code ____________________________________________
def dashboard1(request):

    return render(request,"dashboard1.html")
