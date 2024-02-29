from django.urls import reverse
from django.shortcuts import render
from blogapp.models.BlogModel import blogdata
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from blogapp.image import *
# all these function are used by super user
class Addvalues(TemplateView):
    template_name= "additems.html"
    def post(self,request):
        try:
            blog = blogdata.objects.create(
                title = request.POST["title"],
                desc =  request.POST["description"],
                blogimg = request.FILES["image"]
            )
        except Exception as e:
            return HttpResponse(str(e))
        return HttpResponse("data add successfully")

class showdatablog(TemplateView):
    def get(self,request):
        try:
            data = blogdata.objects.all()
            print(data.values(),"akjsdhfakjshdfkajh")
            context = {"blog": data}
            return render(request,"showdata.html",context)
        except Exception as e:
            return HttpResponse(str(e))

class updatedata(TemplateView):
    def get(self,request,id):
        try:
            data = blogdata.objects.get(id= id)
            context = {"data":data}
            return render(request,"updatepage.html",context)
        except Exception as e:
            return HttpResponse(str(e))
    def post(self , request):
        try:
            blog = blogdata.objects.create(
                title = request.POST["title"],
                desc =  request.POST["description"],
                blogimg = request.FILES["image"]
            )
        except Exception as e:
            return HttpResponse(str(e))
        return HttpResponse("data add successfully")

class deletedata(TemplateView):
    template_name = "showdata.html"
    def get(self ,request,id):
        data = blogdata.objects.get(id=id)
        print(data,"hello ajksdhlfkajhsdlkfjahsdkfjh")
        data.delete()
        print(data,"alksdhfkajhsdflkjahsdlkf")
        return HttpResponseRedirect(reverse("showdatablog"))


class showblog(TemplateView):
    def get(self,request):
        try:
            data = blogdata.objects.all()
            print(data.values(),"akjsdhfakjshdfkajh")
            context = {"blog": data}
            return render(request,"superuser.html",context)
        except Exception as e:
            return HttpResponse(str(e))
       

