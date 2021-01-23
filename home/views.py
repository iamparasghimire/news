from django.shortcuts import render
from blog.models import Post
from django.contrib import messages
from home.models import Contact


def home(request):
    allPosts = Post.objects.all() 
    context = {'allPosts': allPosts}
    print(context)
    return render(request, 'home/index.html',context)


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email,subject, message)

        if len(name)<2 or len(email)<3  or len(message)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,subject=subject, message=message)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        
    return  render(request,'home/contact.html')

def about(request):
    allPosts = Post.objects.all() 
    context = {'allPosts': allPosts}
    print(context)
    return  render(request,'home/about.html',context)

