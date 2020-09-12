from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def SendMail(request):
    resp = json.loads(request.body)
    print(resp)
    #Get data/json in post
    #Parse the data 
    #content = {"name": name,}
    #html_message = loader.render_to_string("email/confirmation.html", content)
    #send_mail("Thank You for Registering with us!","We'd love to invite you to our Orientation. Date and Time are below-mentioned. It's a great opportunity to meet your instructor and mentor. Register for the orientation session.",settings.EMAIL_HOST_USER,[str(to)],html_message=html_message,fail_silently=True,)
    return render(request, 'email.html')

