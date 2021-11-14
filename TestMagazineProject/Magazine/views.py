from django.http import HttpResponse, response, JsonResponse 
from django.shortcuts import render
from Magazine.models import Posts

# Create your views here.
def view(request,*args,**kwargs):
    return HttpResponse('<h1> Hello World </h1>')

#another view
def PostList(request,*arg,**kwargs):
    QSet = Posts.objects.all()
    return HttpResponse(QSet)

def PostJson(request,*args,**kwargs):
    obj = Posts.objects.get(id=1)
    return JsonResponse({"id:":obj.postText})

def Reflect(request, pk: int):
    try:
        obj = Posts.objects.get(id=pk)
    except Posts.DoesNotExist: 
        raise response.Http404()
    return HttpResponse(f"String with ID {obj.id}")
