from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from streetlight import models

# Create your views here.
def login(request):

    #create an initial account
    if not(models.User.objects.filter(username="K").exists()):
      models.User.objects.create(username="K", sex="male",password="123456",email="1274159850@qq.com",tel = "07564540223")

    if not (models.Administrator.objects.filter(name="staff").exists()):
          models.Administrator.objects.create(name = "admin", password="admin")

    #get the user name and the password
    username = request.POST.get("username")
    password = request.POST.get("password")

    #check if the account exist
    if not(models.User.objects.filter(username=username).exists()):
         if not(models.Administrator.objects.filter(name=username).exists()):
             return render(request, 'login.html', {"error_msg": "password wrong"})
         else:
             validPassword = models.Administrator.objects.filter(name=username).first().password
             if password != validPassword:
                 return render(request, 'login.html', {"error_msg": "password wrong"})
             else:
                 return HttpResponseRedirect("/operate/")

    #get the password saved in the database
    validPassword = models.User.objects.filter(username=username).first().password

    if password != validPassword:
        return render(request, 'login.html', {"error_msg": "password wrong"})


    myResponse =  render(request, 'News.html')
    myResponse.set_cookie("username",username,max_age = 1*60*60)
    return myResponse

def news(request,id):
    rk = request.COOKIES.get('username')
    if not rk:
        return redirect('/login/')

    if not(models.Job.objects.filter(requirment="man")):
        models.Job.objects.create(salary=100,email="1234567@qq.com",city="Glasgow",requirment="man",)

    jobs = models.Job.objects.get()

    return 1