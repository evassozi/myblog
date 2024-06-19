from django.shortcuts import render
from .models import Feedback
#create your views here:

def feedback(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    feedback = Feedback(name=name, email=email, subject=subject, message=message)
    feedback.save()

    return render(request=request, template_name='success.html')