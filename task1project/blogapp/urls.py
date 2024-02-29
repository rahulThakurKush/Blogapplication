from django.urls import path
from blogapp.views.userview import SignUp,verifiyotp,login
from blogapp.views.showdata import Addvalues,showdatablog,updatedata,deletedata,showblog
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path("signup/",SignUp.as_view(),name = "signup"),
    path("login/",login.as_view(),name = "login"),
    path("verifyotp/",verifiyotp.as_view(),name = "otpverification"),
    path("addvalues/",Addvalues.as_view(),name = "addvalues"),
    path("showdatablog/",showdatablog.as_view(),name = "showdatablog"),
    path("updatedata/<int:id>/",updatedata.as_view(),name = "updatedata"),
    path("deletedata/<int:id>/",deletedata.as_view(),name = "deletedata"),
    path("showblog/",showblog.as_view(),name = "showblog")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)