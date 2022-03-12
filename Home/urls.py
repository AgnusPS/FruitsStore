from Home import views
from django.urls import path
app_name = 'Home'

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("home/",views.CustomerHome,name="CustomerHome"),
    path("myprofile/",views.myprofile,name="myprofile"),
    path("editprofile/",views.editprofile,name="editprofile"),
]
     