from django.shortcuts import render
from .models import Blog
import markdown


# Create your views here.
def home(request):
    all_blogs = Blog.objects.all()
    context = {"blogs":all_blogs}

    return render(request,
                  template_name="blog/home.html",
                  context=context)


def details(request, id):
    blog = Blog.objects.get(id=id)
    content = markdown.markdown(blog.content_markdown)
    context = {"blog":blog, "content":content}

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



