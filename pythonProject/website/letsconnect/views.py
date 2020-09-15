from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from letsconnect.models import Userprofile
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        context={}
        # validation
        if pass1 != pass2:
            context["status"] = "alert-danger"
            context["message"] = "Password Doesn't match"
            return render(request, 'Register.html', context)
        elif User.objects.filter(username=username).exists():
            context["status"] = "alert-primary"
            context["message"] = "Username already exists"
            return render(request, 'Register.html', context)
        elif User.objects.filter(email=email).exists():
            context["status"] = "alert-primary"
            context["message"] = "Email-id already exists"
            return render(request, 'Register.html', context)
        else:
            user = User.objects.create_user(username=username, email=email, password=pass1)
            user.save();
            context["status"] = "alert-success"
            context["message"] = "User registered form Try Logging in to experience letsconnect"
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')



def message(request):
    return render(request, 'message.html')

def faq(request):
    return render(request, 'faq.html')

def contactus(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')



def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            return render(request, 'setpassword.html')
        else:
            message = " Email id Is Not Found!!!"
            return render(request, 'forgotpassword.html', {'message':message} )
    else:
        return render(request, 'forgotpassword.html')


def setpassword(request):
    if request.method == 'POST':
        newpass1 = request.POST['password1']
        newpass2 = request.POST['password2']
        username = request.POST['username']
        context = {}
        if newpass1 != newpass2:
            context["status"] = "alert-danger"
            context["message"] = "Password Doesn't match"
            return render(request, 'setpassword.html', context)
        elif User.objects.filter(username=username).exists():
            usr = User.objects.get(username=username)
            usr.set_password(newpass1)
            usr.save();
            context["status"] = "alert-success"
            context["message"] = "Password updated...!!!!! go back to home and login"
            return render(request, 'setpassword.html', context)

        else:
            context["status"] = "alert-danger"
            context["message"] = "User Not Found"
            return render(request, 'setpassword.html', context)


    else:
        return render(request, 'setpassword.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect(hom3)
        else:
            error_message ="Invalid Credentials !!!"
            return render(request, 'login.html', {'error': error_message})
    else:
        return render(request, 'login.html')

def hom3(request):
    return render(request, 'hom3.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def updateprofile(request):
    if request.method == 'POST':
        context= {}
        username=request.POST['username']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        email=request.POST['email']
        aboutyou = request.POST['bio']
        cpy= request.POST['button']
        usp = Userprofile.objects.get(user__id=request.user.id)
        psusername=usp.username
        paddress = usp.address
        pphone_number = usp.phone_number
        pAbout_you = usp.About_you
        usr = User.objects.get(id=request.user.id)
        pemail = usr.email
        if usp is not None:
            if cpy == 'Yes':
                newpass_1 = request.POST['newpassword1']
                newpass_2 = request.POST['confirmpassword1']
                current=request.POST['currentpassword']
                check=User.check_password(usr,raw_password=current)
                if check:
                    if newpass_1 != newpass_2:
                        context["status"] = "alert-danger"
                        context["message"] = "Password Doesn't match"
                        return render(request, 'updateprofile.html', context)
                    else:
                        usr.set_password(newpass_1)
                        usr.save();
                        if username == '':
                            usp.username=psusername
                        else:
                            usp.username=username
                        if phone_number == '':
                            usp.phone_number = pphone_number
                        else:
                            usp.phone_number = phone_number
                        if address == '':
                            usp.address = paddress
                        else:
                            usp.address = address
                        if email == '':
                            usp.email = pemail
                        else:
                            usp.email = email
                        if aboutyou == '':
                             usp.About_you = pAbout_you
                        else:
                            usp.About_you = aboutyou
                        usp.save();
                        context["status"] = "alert-success"
                        context["message"] = "Password and Details updated"
                        return render(request, 'updateprofile.html', context)
                else:
                    context["status"] = "alert-danger"
                    context["message"] = "Current password Doesn't match"
                    return render(request, 'updateprofile.html', context)
            else:
                if username == '':
                    usp.username = psusername
                else:
                    usp.username = username
                if phone_number == '':
                    usp.phone_number = pphone_number
                else:
                    usp.phone_number = phone_number
                if address == '':
                    usp.address = paddress
                else:
                    usp.address = address
                if email == '':
                    usr.email = pemail
                else:
                    usr.email = email
                if aboutyou == '':
                    usp.About_you = pAbout_you
                else:
                    usp.About_you = aboutyou
                usp.save();
                usr.save();
                context["data"]=usp
                context["status"]="alert-success"
                context["message"] = "Profile Updated with out change in password"
                return render(request, 'updateprofile.html', context)
        else:
            context["status"] = "alert-danger"
            context["message"] = "Profile not found with given Details!!!!"
            return render(request, 'updateprofile.html', context)
    else:
        context={}
        data = Userprofile.objects.get(user__id=request.user.id)
        context["data"] = data
        return render(request, 'updateprofile.html', context)


def profilephotoupload(request):
    context={}
    data = Userprofile.objects.get(user__id=request.user.id)
    context["data"] = data
    return render(request, 'profilephotoupload.html', context)

def contactform(request):
    return render(request, 'contactform.html')


