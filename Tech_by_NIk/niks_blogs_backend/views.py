from django.shortcuts import render
from .models import Image,Post
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def index(request):
    post_data = Post.objects.all()
    post = Post.objects.filter().order_by('-id')[:6]
    post_in_ascending_order = reversed(post)
    return render(request,'html_files/index.htm',{"post":post})



def DetalView(request,id):
    post = get_object_or_404(Post,id=id)
    post_data = Post.objects.all()
    photos = Image.objects.filter(post=post)
    return render(request,'html_files/detail.htm',{"post":post,"photos":photos,'post_data':post_data})


def Blogs(request):
    post = Post.objects.all()
    return render(request,'html_files/Blogs.htm',{"post":post})


def About(request):
    return render(request,'html_files/About.htm')


def Contact(request):
    return render(request,'html_files/Contact.htm')

def search_data(request):
    pass