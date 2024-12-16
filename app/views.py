from django.shortcuts import render, redirect
from . models import*
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
#// start Views for all html pages
def index(request):
    # // get ip adress
    def get_ip(request):
        adress = request.META.get('HTTP_X_FORWARDED')
        if adress:
            ip = adress.split(',')[-1].sprit()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = User(user=ip)
    result = User.objects.filter(Q(user__icontains=ip))

    if len(result) == 1:
        u.save()
        pass
    elif len(result) > 1:
        u.save()
        pass
    else:
        u.save()
    count = User.objects.all().count()

    all_patient = patinet.objects.all().count()
    all_dr = regDoctors.objects.all().count()
    drlist = regDoctors.objects.all()[:4]
    rat = Rating.objects.all()

    return render(request, "app/index.html", {'drlist':drlist, 'count':count, 'total_pat':all_patient, 'total_dr':all_dr, 'rat':rat, 'visitor':count})

def about(request):
    drlist = regDoctors.objects.all()[:4]
    pat = UserMaster.objects.filter(role='Patient')
    return render(request, "app/about.html",{'drlist':drlist,'pat':pat})

def service(request):
    drlist = regDoctors.objects.all()
    pat = UserMaster.objects.filter(role='Patient')
    return render(request, "app/service.html",{'drlist':drlist,'pat':pat})

def contact(request):
    drlist = regDoctors.objects.all()[:4]
    pat = UserMaster.objects.filter(role='Patient')
    return render(request, "app/contact.html",{'drlist':drlist,'pat':pat})

def appointment(request):
    drlist = regDoctors.objects.all()
    pat = UserMaster.objects.filter(role='Patient')
    return render(request, "app/appointment.html",{'drlist':drlist, 'pat':pat})

def appointmentPage(request):
    return render(request, "app/appointment.html")

def team(request):
    drlist = regDoctors.objects.all()
    return render(request, "app/team.html",{'drlist':drlist})

def feature(request):
    return render(request, "app/feature.html")

def testimonial(request):
    rat = Rating.objects.all()
    return render(request, "app/testimonial.html", {'rat':rat})

def error(request):
    return render(request, "app/404.html")

def RegForm(request):
    return render(request, "app/form/index.html")

def LogForm(request):
    return render(request, "app/form/login.html")

def userSignup(request):
    return render(request, "app/userSignup.html")

def userLogin(request):
    return render(request, "app/login.html")

#// End Views for all html pages
# // get appointments
def GetAppointment(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        doctor = request.POST['doctor']
        chose_date = request.POST['chose_date']
        description = request.POST['description']

        getAppointment.objects.create(
                                    fname=fname, 
                                    lname=lname, 
                                    email=email, 
                                    contact=contact, 
                                    doctor=doctor, 
                                    chose_date=chose_date, 
                                    descrption=description
                                    )

        message = "Appointment Recived Successfully"
        return render(request, "app/appointment.html", {'msg':message })

#// user userProfile 
def userProfile(request):   
    email = request.session.get('email')
    appointment = getAppointment.objects.filter(email=email)
    pat = patinet.objects.get(email=email)
    return render(request, "app/userProfile.html",{'app':appointment,'pat':pat})

#// user sigin 
def userSignin(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['Cpassword']
        contact = request.POST['contact']
        about = request.POST['about']
        img = request.FILES['img']

        user = UserMaster.objects.filter(email=email)
        if user:
            message = "You are alrady registerd."
            return render(request, "app/login.html", {'msg':message})
        else:
            if password == Cpassword:
                
                newUser = UserMaster.objects.create(
                    name=name,
                    email=email,
                    role="Patient",
                    password=password,
                )

                newPat = patinet.objects.create(
                    userId=newUser,
                    name=name,
                    email=email, 
                    contact=contact,
                    about=about,
                    img=img,
                )

                message = "Signup successfully,"
                return render(request, "app/login.html",{'succ':message})
            else:
                message = "Confirm password dose not matched."
                return render(request, "app/userSignup.html", {'msg':message})

#// login user 
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
  
        user = UserMaster.objects.get(email=email)

        if user and user.role == "Patient":
            if user.password == password:
                pat = patinet.objects.get(userId=user)
                request.session['name'] = user.name
                request.session['email'] = user.email
                request.session['role'] = user.role
                request.session['contact'] = pat.contact
                request.session['img'] = pat.img.url
                request.session['patient'] = "patient"
                return redirect('index')
            else:
                message = "Wrong Password."
                return render(request, "app/login.html",{'msg':message})
        else:
            message = "Wrong Email."
            return render(request, "app/login.html",{'msg':message})

#// doctor profile page
def DrProfile(request):
    return render(request, "app/dashbord/pages-profile.html",)

# // Doctor registation
def DrRegister(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        re_pass = request.POST['re_pass']

        #// chack user 
        user = UserMaster.objects.filter(email=email).first()

        if user:
            message = "user alrady registerd"
            return render(request, "app/form/login.html", {'mdg':message})
        else:
            if password == re_pass:
                #// add new user in userMaster Module
                newUser = UserMaster.objects.create(
                    name=name,
                    email=email,
                    role= "Doctor",
                    password=password,
                )
                # add new doctor 
                newDr = regDoctors.objects.create(
                    userId=newUser,
                    name=name,
                    email=email,
                )
                message = "Doctor register successfully."
                return render(request, "app/form/login.html", {'mdg':message})
            else:
                message = "Confirm password dose not matched."
                return render(request, "app/form/index.html",{'msg':message})

# // Doctors login
def DrLogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass']

        # chack user
        user = UserMaster.objects.get(email=email)

        if user and user.role == "Doctor":
            if user.password == password:

                dr = regDoctors.objects.get(userId=user)

                request.session['name'] = user.name
                request.session['email'] = user.email
                request.session['password'] = user.password
                request.session['role'] = user.role
                request.session['id'] = user.id
                request.session['doctor'] = "doctor"

                return render(request, "app/dashbord/pages-profile.html", {'dr':dr})
            else:
                message = "Wrong password.."
                return render(request, "app/form/login.html", {'msg':message})
        else:
            message = "Wrong email."
            return render(request, "app/form/login.html", {'msg':message})

#// get dr info in profile
def DrInfo(request, pk):
    user = UserMaster.objects.get(pk=pk)
    dr = regDoctors.objects.get(userId=user)
    patt = getAppointment.objects.filter(doctor=dr.name)
    return render(request, "app/dashbord/pages-profile.html", {'dr':dr,'patt':patt})

#/ Update Dr info
def UpdateInfo(request, pk):
    dr = regDoctors.objects.get(userId=pk)
    
    dr.name = request.POST.get('name')
    dr.title = request.POST.get('title')
    dr.degree = request.POST.get('degree')
    dr.livesIn = request.POST.get('livesIn')
    dr.workAt = request.POST.get('workAt')
    dr.froms = request.POST.get('froms')
    dr.contact = request.POST.get('contact')
    dr.facebook = request.POST.get('facebook')
    dr.x = request.POST.get('x')
    dr.linkedin = request.POST.get('linkedin')
    dr.save()

    # url = f'/DrInfo/{pk}'
    # return render(request, "app/dashbord/pages-profile.html", {'dr':dr})
    return redirect(f'/DrInfo/{pk}')

# Update doctor's profile
def updateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    dr = regDoctors.objects.get(userId=user)

    newDP = request.FILES.get('profile')
    if newDP:
        if dr.profile:
            dr.profile.delete()
        dr.profile = newDP
    dr.save()
    # return render(request, "app/dashbord/pages-profile.html")
    return redirect(f'/DrInfo/{pk}')

# // patain logout 
def Patlogout(request):
    request.session.flush()
    return redirect('index')


# // doctor logout 
def Drlogout(request):
    request.session.flush()
    return redirect('index')

### --- appointment status ---###
def status(request, pk):
    app = getAppointment.objects.get(pk=pk)
    return render(request, "app/dashbord/status.html",{'app':app})

def appStatus(request, pk):
    app = getAppointment.objects.get(pk=pk)

    app.status = request.POST['role']
    app.visit = request.POST['visit']

    app.save()
    
    # return redirect('dashIndex')
    return render(request, "app/dashbord/pages-profile.html")

# rating 
def ratingPage(request):
    return render(request, "app/rating.html")

def getRating(request):
    if request.method == "POST":
        img = request.FILES['img']
        name = request.POST['name']
        title = request.POST['title']
        description = request.POST['description']

        Rating.objects.create(
            img=img,
            name=name,
            title=title,
            description=description,
        )
        return redirect('index')
#// Admin 
def adminIndex(request):
    return render(request, "app/admin/index.html")

def AdminLogin(request):
    return render(request, "app/admin/pages-sign-in.html")

def AdminSignin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if email == "admin":
            if password == "1234":
                request.session['email'] = "adminemail"
                request.session['password'] = "1234"

                all_visitors = User.objects.all().count()
                all_appoint = getAppointment.objects.all().count()
                all_appoints = getAppointment.objects.all()
                all_rating = Rating.objects.all()
                all_user = UserMaster.objects.all()
                all_doctor = regDoctors.objects.all().count()
                all_doctors = UserMaster.objects.filter(role="Doctor")
                all_patinet = patinet.objects.all().count()
                all_patinets = UserMaster.objects.filter(role="Patient")
                return render(request, "app/admin/index.html",{
                    'visit':all_visitors,
                    'appoint':all_appoint,
                    'appoints':all_appoints,
                    'user':all_user,
                    'doctor':all_doctor,
                    'doctors':all_doctors,
                    'patinet':all_patinet,
                    'patinets':all_patinets,
                    'rating':all_rating,
                })
            else:
                message = "Wrong Password"
                return render(request, "app/admin/pages-sign-in.html",{'msg':message})
        else:
            message = "Wrong Email"
            return render(request, "app/admin/pages-sign-in.html",{'msg':message})

# doctor verifications
def drVerification(request, pk):
    dr = UserMaster.objects.get(pk=pk)
    return render(request, "app/admin/status.html", {'dr':dr})

def drVerifi(request, pk):
    dr = UserMaster.objects.get(pk=pk)
    dr.is_verified = request.POST['role']
    dr.save()
    return redirect('adminIndex')

def drDelete(request, pk):
    dr = UserMaster.objects.get(pk=pk)
    dr.save()
    return redirect('adminIndex')

