from django.shortcuts import render
from .models import Post




def bloghome(request):
    allPosts = Post.objects.all() 
    context = {'allPosts': allPosts}
    return render(request, 'blog/bloghome.html', context) 
   

def blogpost(request, sno):
    allPosts = Post.objects.all() 

  
    post = Post.objects.filter(sno=sno).first()
    context = {'post': post,'allPosts': allPosts}
    return render(request, 'blog/blogpost.html', context) 