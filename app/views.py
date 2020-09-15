from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def SendMail(request):
    resp = json.loads(request.body)
    if resp["payload"]["payment"]["entity"]["notes"]["course_code"] == "FF66YEH":
        content = {"name": resp["payload"]["payment"]["entity"]["notes"]["name"]}
        to = resp["payload"]["payment"]["entity"]["notes"]["email"]
        print(to)
        html_message = loader.render_to_string("confirmation.html", content)
        send_mail(
            "Thank You for Registering with us!",
            "We'd love to invite you to our Orientation. Date and Time are below-mentioned. It's a great opportunity to meet your instructor and mentor. Register for the orientation session.",
            settings.EMAIL_HOST_USER,
            [str(to)],
            html_message=html_message
            fail_silently=False,
        )
    else:
        print("Payment failed!")
    return render(request, "email.html")

