import random
from  task1project.settings import *
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_otp_via_mail(email,first_name):
    print(75646745635467367456435346757674635234657468575653)
    message = make_otp()
    name = first_name
    context = {
        "OTP":message,
        "Name":name,
    }
    print(111211111122254656534122143565765343453)
    temp = render_to_string('otp.html', context)
    msg = EmailMultiAlternatives("", temp, EMAIL_HOST_USER, [email])
    msg.content_subtype = 'html'
    msg.send()
    print('mail sent opt')
    return message



def make_otp():
    var = "".join(str(random.randint(0,9))for _ in range(6))
    return var