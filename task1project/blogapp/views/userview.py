import http
from django.shortcuts import render
from blogapp.models.UserModel import UserModel
from django.views.generic import TemplateView
from django .contrib.auth.hashers import check_password
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from blogapp.send_mail import send_otp_via_mail

class SignUp(TemplateView):
    template_name = "signup.html"
    def post(self , request):
        try:
            print(request.POST,"-------------------------")
            user = UserModel.objects.create(
                first_name= request.POST["first_name"],
                last_name = request.POST["last_name"],
                username = request.POST["username"],
                email = request.POST["email"])
            user.set_password(request.POST["password"])
            otp = send_otp_via_mail(request.POST["email"],request.POST["first_name"])
            request.session['otp']=otp
            request.session['email']=request.POST["email"]
            # request.session['is_varified']=user.is_varified
            user.otp = otp
            user.save()
        except Exception as e:
            return HttpResponse(str(e))
        return HttpResponseRedirect(reverse("otpverification"))

class login(TemplateView):
    template_name = "login.html"
    def post(self,request):
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = UserModel.objects.get(email = email)
        except Exception as e:
            return HttpResponse(str(e))
        check_pass = check_password(password ,user.password)
        if user and user.is_varified:
            # login(request, user)
            if user.is_superuser:
                return   HttpResponseRedirect(reverse("showdatablog"))
            else:
                return HttpResponseRedirect(reverse("showblog"))
        else:
            return HttpResponse("invalid email or password...")
        

class verifiyotp(TemplateView):
    template_name = "otpverification.html"
    def post(self , request):
        otp = request.POST['otp']
        email = request.session.get("email")
        user = UserModel.objects.get(email=email)
        try:
            # user = UserModel.objects.get(verified = verify)
            if otp == user.otp:
                user.is_varified = True
                user.save()
                return HttpResponseRedirect(reverse("login"))
            else:
                return HttpResponse("otp is not valid")
        except Exception as e:
            return HttpResponse(str(e))




