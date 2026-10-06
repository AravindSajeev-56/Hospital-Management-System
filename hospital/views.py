from django.shortcuts import render,redirect
from .models import UserComplaints
from .models import department
from .models import Doctors
from .models import hospital
from .models import vir
from .models import online
from .models import tokenbooking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    return render(request, 'login.html')

def user_login(request):
    if request.user.is_authenticated:  # Use request.user instead of session
        return redirect('home')
    
    if request.method == 'POST':
        uname = request.POST["username"]
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request)  # Django’s built-in login
            return redirect('home')
        else:
            return render(request, "login.html", {'msg1': 'Invalid user credentials'})
    
    return render(request, "login.html")


def logout_view(request):
    logout(request)  # Django's built-in logout
    return redirect('login')

def sign_up(request):
    uform = UserCreationForm(request.POST)  # ❌ Form should be initialized inside POST block
    if request.method == "POST":
        if uform.is_valid():
            uname = uform.cleaned_data.get('username')
            pwd = uform.cleaned_data.get('password1')
            user1 = User.objects.create_user(username=uname, password=pwd)
            user1.save()
            return redirect('login')
    else:
        form1 = UserCreationForm()
        return render(request, 'sign_up.html', {'form': form1})
    return render(request, 'sign_up.html', {'form': uform})


def resetPassword(request):
    responseDic={}
    try:
        usern = request.POST['uname']
        recepient=request.POST['email']
        pwd=request.POST['password']
        #subject
        try:
            user=User.objects.get(username=usern)
            if user is not None:
                user.set_password(pwd)
                user.save()
                #send
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,"login.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["errmsg"]="Email doesnt exit"
            return render(request,"resetpassword.html",responseDic)
    except Exception as e:
        print(e)
        return render(request,"resetpassword.html",responseDic)

def home(request):
    if 'username' in request.session:
        return render(request,'home.html')
    return redirect('login')

def about(request):
    return render(request,'about.html')

def mycomplaints(request):
    responseDic = {}
    if request.method == "POST":
        em = request.POST['email']  
        co = request.POST['comment'] 
        responseDic["msg2"] = em
        responseDic["msg3"] = co
        out = UserComplaints(email=em, comment=co)
        out.save()
        responseDic["msg1"] = "Complaint Successfully Registered"
        return render(request, "about.html", responseDic)
    else:
        return render(request, "about.html")

def mydepartment(request):
    dict_dept={
        'deptkey':department.objects.all()
    }
    return render(request,"department.html",dict_dept)

def mydoctors(request):
    dict_docs = {}
    if request.method == "POST":
        department_name = request.POST['department']
        doctors = Doctors.objects.select_related('dep_name').filter(dep_name__dep_name=department_name)
        dict_docs['doctkey'] = doctors.values()
        return render(request, "doctors.html", dict_docs)
    else:
        return render(request, "doctors.html")

def myhospital(request):
    dict_docs={
        'doctkey':hospital.objects.all()
    }
    return render(request,"ourhospital.html",dict_docs)

def myaidoctor(request):
    responseDic = {}
    if request.method == "POST":
        sym1 = request.POST['symptom1']
        sym2 = request.POST['symptom2']
        sym3 = request.POST['symptom3']
        sym4 = request.POST['symptom4']
        
        if (sym1 == 'Chest Pain' and 
            sym2 == 'Vision Problems' and 
            sym3 == 'Headaches' and 
            sym4 == 'Flushing'):
            responseDic["msg1"] = "Hypertension (High Blood Pressure)"
            responseDic["msg2"] = "Hypertension, or high blood pressure, often presents with subtle or no symptoms, which is why it is sometimes called the silent killer."
            responseDic["msg3"] = "Disease : "
            responseDic["msg4"] = "Disease Description : "
            responseDic["msg5"] = "Visit Hospital, Conduct Details : 8645239657 "
        elif (sym1 == 'Dark Urine' and 
            sym2 == 'Pale Stools' and 
            sym3 == 'Joint Pain' and 
            sym4 == 'Jaundice'):
            responseDic["msg1"] = "Hepatitis B"
            responseDic["msg2"] = "Hepatitis B is a liver infection caused by the hepatitis B virus (HBV). Symptoms can vary from mild to severe and may appear 1 to 4 months after exposure to the virus"
            responseDic["msg3"] = "Disease : "
            responseDic["msg4"] = "Disease Description : "
            responseDic["msg5"] = "Visit Hospital, Conduct Details : 8645239657 "
        elif (sym1 == 'Skin changes' and 
            sym2 == 'Pain' and 
            sym3 == 'Swelling' and 
            sym4 == 'Thickening'):
            responseDic["msg1"] = "Breast Cancer"
            responseDic["msg2"] = "Many of these symptoms can also be caused by noncancerous conditions, but it's important to see a healthcare professional if you notice any changes in your breast tissue. Early detection is key to successful treatment."
            responseDic["msg3"] = "Disease : "
            responseDic["msg4"] = "Disease Description : "
            responseDic["msg5"] = "Visit Hospital, Conduct Details : 8645239657 "
        else:
            responseDic["msg1"] = "Please consult a doctor for further advice."
            responseDic["msg2"] = "Conduct Details : 8645239657"
        
        return render(request, "aidoctor.html", responseDic)
    
    # Handle GET requests
    return render(request, "aidoctor.html")

@login_required
def myvirtualdoctor(request):
    responseDic = {}
    if request.method=="POST":
        try:
            na = request.POST['name']
            ag = request.POST['age']
            ph = request.POST['phone']
            em = request.POST['email']
            de = request.POST['department']
            responseDic["output1"]=na
            responseDic["output2"]=ag
            responseDic["output3"]=ph
            responseDic["output4"]=em
            responseDic["output5"]=de
            out=vir(p_name=na,p_age=ag,p_phone=ph,p_email=em,p_department=de)
            out.save()
            responseDic["msg1"] = "Created"
            return render(request, "virout.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["msg1"] = "Try again"
            return render(request, "virtualdoctor.html", responseDic)
    else:
        return render(request, "virtualdoctor.html")

def mypayment(request):
    responseDic = {}
    if request.method=="POST":
        try:
            na = request.POST['name']
            an = request.POST['cardnumber']
            em = request.POST['expmonth']
            ey = request.POST['expyear']
            cv = request.POST['cvv']
            out=online(c_name=na,c_number=an,c_month=em,c_cvv=cv,c_year=ey)
            out.save()
            responseDic["msg1"] = "Payment Complete"
            responseDic["msg2"] = "Please wait... You will receive a call on WhatsApp."
            return render(request, "payment.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["msg1"] = "Try again... "
            return render(request, "payment.html", responseDic)
    else:
        return render(request, "payment.html")
    
@login_required    
def mybooking(request):
    responseDic = {}
    if request.method == "POST":
        try:
            na = request.POST['name']
            ag = request.POST['age']
            pl = request.POST['place']
            ph = request.POST['phone']
            de = request.POST['department']
            do = request.POST['doctor']
            da = request.POST['date']
            responseDic["output1"] = na
            responseDic["output2"] = ag
            responseDic["output3"] = pl
            responseDic["output4"] = ph
            responseDic["output6"] = de
            responseDic["output7"] = do
            responseDic["output8"] = da
            out = tokenbooking(b_name=na, b_age=ag, b_place=pl, b_phone=ph, b_department=de, b_doctor=do, b_date=da)
            out.save()
            responseDic["msg1"] = "Booking Confirmed"

            return render(request, "conbooking.html", responseDic)
        except Exception as e:
            print(e)
            responseDic["msg1"] = "Try again..."
            return render(request, "conbooking.html", responseDic)
    else:
        return render(request, "booking.html")
    



