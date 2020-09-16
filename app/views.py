from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import loader
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

@csrf_exempt
def SendMail(request):
    resp = json.loads(request.body)
    if resp["payload"]["payment"]["entity"]["notes"]["course_code"] == "FF66YEH":
        content = {"name": resp["payload"]["payment"]["entity"]["notes"]["name"]}
        to = resp["payload"]["payment"]["entity"]["notes"]["email"]
        html_message = loader.render_to_string("confirmation.html", content)
        message = EmailMultiAlternatives(
            'Thank You for registering with us!',            
            "We'd love to invite you to our Orientation. Date and Time are below-mentioned. It's a great opportunity to meet your instructor and mentor. Register for the orientation session.",
            settings.EMAIL_HOST_USER,
            [str(to)],          
        )
        message.attach_alternative(html_message, 'text/html')
        message.send()
    else:
        print("Payment failed!")
    return render(request, "email.html")

@csrf_exempt
def send_mail(request):
    record = Record()
    record.name = request.POST.get("name")
    record.email = request.POST.get("_replyto")
    record.number = request.POST.get("number")
    record.whatsapp = request.POST.get("whatsapp")
    plain_message = loader.render_to_string("text.html", {"name": record.name})
    html_message = loader.render_to_string("free_course.html", {"name": record.name})
    message = EmailMultiAlternatives(
        "Welcome - SkillSafari",
        plain_message,
        settings.EMAIL_HOST_USER,
        [str(record.email)],
    )
    message.attach_alternative(html_message, 'text/html')
    message.send()
    record.save()

def view(request):
    context = {
        "records": Record.objects.all()
    }
    return render(request, 'index.html', context)