from django.http import HttpResponse, response
from django.shortcuts import render
from Magazine.models import Posts

# Create your views here.
def view(request,*args,**kwargs):
    return HttpResponse('<h1> Hello World </h1>')

#another view
def PostList(request,*arg,**kwargs):
    QSet = Posts.objects.all()
    return HttpResponse(Qset)
    
