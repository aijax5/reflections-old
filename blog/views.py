from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    return HttpResponse('Hello this is the landing page')

def individual_post(request):
    recent_post = Post.objects.get(id__exact=2)
    return HttpResponse(recent_post.title + ': ' + recent_post.content)