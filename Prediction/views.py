from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from Prediction.forms import UserForm,UserProfileInfoForm
from django.urls import reverse


from .forms import Predict_Form,UserProfileInfo
import joblib
import pickle
from django.conf import settings
# Create your views here.

def about(request):
    return render(request,"accounts/about.html",{})

def precaution(request):
    return render(request,"accounts/index.html")

def Res(request):
    predicted = False
    predictions = {}

    if request.method == 'POST':
        form = Predict_Form(data=request.POST)
        profile = get_object_or_404(UserProfileInfo,user = request.user)
        print("Profile............................")
        print(profile)

        if form.is_valid():
            # Getting all data of user/patient
            features = [[form.cleaned_data['age'], form.cleaned_data['sex'], form.cleaned_data['cp'],
                         form.cleaned_data['resting_bp'], form.cleaned_data['serum_cholesterol'],
                         form.cleaned_data['fasting_blood_sugar'], form.cleaned_data['resting_ecg'],
                         form.cleaned_data['max_heart_rate'], form.cleaned_data['exercise_induced_angina'],
                         form.cleaned_data['st_depression'], form.cleaned_data['st_slope'],
                         form.cleaned_data['number_of_vessels'], form.cleaned_data['thallium_scan_results']]]
            print(features)
            # standard_scalar = GetStandardScalarForHeart()
            # features = standard_scalar.transform(features)
            pred = form.save(commit=False)

            dt = joblib.load('decision.sav')
            x = features
            print("Decision = ", dt.predict(x))
            dct =dt.predict(x)

            lgr = joblib.load(('logreg.sav'))
            scale = joblib.load("scaler.sav")
            y = scale.transform(x)
            print(y)
            print("Logistic Regression = ", lgr.predict(y))
            print(lgr.predict_proba(y))
            z = lgr.predict_proba(y)
            n= z[0][-1] * 100
            a = str(round(n,2))
            yes = float(a)
            b="%"


            nop = 100-float(a)
            no = nop

            l=lgr.predict(y)
            lgres = str(l[0])
            res = a + b
            if lgres==1:
                pred.target = 1
            else:
                pred.target =0

            pred.profile = profile
            pred.pred_percentage = res

            pred.save()

            print(lgres)



    return render(request,'result.html',{'ans':res,'lg':lgres,'no':no,'yes':yes})



def Home(request):
    context = {}
    context['form'] = Predict_Form()
    return render(request,"accounts/Home.html",context)
def Logout(request):
    return render(request,"accounts/logout.html",{})
# Registration Page view
def Registration(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            print("user pass",user.password)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,"accounts/Register.html",
                                        {"user_form":user_form,
                                         "profile_form": profile_form,
                                        "registered":registered})
# User Login Page views

def Ulogin (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("Home"))
            else:
                return HttpResponse("Account is not acitve")
        else:
            print("Login Failed")
            return HttpResponse("You Entered Invalid Details!")
    else:
        return render(request,"accounts/Login.html",{})


#After Login
@login_required
def Success(request):
    return HttpResponse("Logged in Succssfully!")

# Logout
@login_required
def Ulogout(request):
    logout(request)
    return render(request,'accounts/Home.html',{})
