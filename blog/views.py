from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    all_blogs = Blog.objects.all()
    context = {"blogs":all_blogs}

    return render(request,
                  template_name="blog/home.html",
                  context=context)


def details(request, id):
    blog = Blog.objects.get(id=id)
    context = {"blog":blog}

    return render(request,
                  template_name="blog/details.html",
                  context=context)

def about(request):
    context = {}
    return render(request,
                  template_name="about.html",
                  context=context)

def contact(request):
    context = {}
    return render(request,
                  template_name="contact.html",
                  context=context)



