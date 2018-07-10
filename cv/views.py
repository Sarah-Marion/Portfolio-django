from django.shortcuts import render,redirect
from .email import send_welcome_email
from django.contrib import messages
from .models import Project, Cv, Info, Technique 

# Create your views here.
def index(request):
    title = "Sarah Marion-FullStack Developer"
    infos = Info.objects.all()
    technique = Technique.objects.all()
    projects = Project.objects.all()
    cv = Cv.objects.all()
    for inf in infos:
        info = inf
    for i in infos:
        cv = i
        
    return render(request, 'index.html',{'title': title, 'projects': projects, 'cv': cv, 'info': infos, 'technique': technique})


def contact(request):
    if request.method == 'POST' and 'message' in request.POST:
        email_content = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = "NAME: "+name + " " + "EMAIL: " + email
        send_welcome_email(subject, email_content)
        messages.success(request, 'Email sent successfully')
    return redirect(index)