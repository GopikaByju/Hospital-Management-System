from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from secondapp.forms import DepartmentForm, GalleryForm, FacilitiesForm, DoctorsForm, BookingForm, CareersForm
from secondapp.models import DepartmentModel, GalleryModel, FacilitiesModel, DoctorsModel, BookingModel, CareersModel, \
    Person


# Create your views here.
def contactview(request):
    return render(request,'contact.html')
def homeview(request):
    return render(request,'home.html')
def aboutview(request):
    return render(request,'about.html')
def departmentsview(request):
    dept=DepartmentModel.objects.all()
    return render(request,'departments.html',{'dept':dept})
def doctorsview(request):
    doc = DoctorsModel.objects.all()
    return render(request,'doctors.html',{'doc':doc})
def bookingview(request):
    return render(request,'booking.html')
def facilitiesview(request):
    fac=FacilitiesModel.objects.all()
    return render(request,'facilities.html',{'fac':fac})
def CareersView(request):
    car = CareersModel.objects.all()
    return render(request,'careers.html',{'car':car})
def galleryview(request):
    gal = GalleryModel.objects.all()
    return render(request,'gallery.html',{'gal':gal})


def DepartmentView(request):
    if request.method=='POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
    form=DepartmentForm()
    return render(request,'deptadminadd.html',{'form':form})

def DepartmentDisplayView(request):
    dept = DepartmentModel.objects.all()
    return render(request, 'deptadmindisplay.html', {'dept': dept})

def DepartmentSingleDisplay(request,id):
    dept=DepartmentModel.objects.get(id=id)
    return render(request,'deptsingleview.html',{'dept':dept})

def DepartmentDetailsView(request,id):
    dept = get_object_or_404(DepartmentModel, id=id)
    doctors = dept.doctors.all()
    return render(request, 'deptdetails.html', {'dept': dept,'doctors': doctors})


def DepartmentEdit(request,id):
    dept = get_object_or_404(DepartmentModel, id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('deptadmindisplay')
    form = DepartmentForm(instance=dept)
    return render(request, 'deptadminedit.html', {'form': form})

def DepartmentDelete(request,id):
    dept = get_object_or_404(DepartmentModel, id=id)
    dept.delete()
    return redirect('deptadmindisplay')


def GalleryaddView(request):
    if request.method=='POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            form.save()
    form=GalleryForm()
    return render(request,'galleryadminadd.html',{'form':form})

def GallerydisplayView(request):
    gal = GalleryModel.objects.all()
    return render(request, 'galleryadmindisplay.html', {'gal': gal})

def GalleryEdit(request,id):
    gal = get_object_or_404(GalleryModel, id=id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, instance=gal)
        if form.is_valid():
            form.save()
            return redirect('galleryadmindisplay')
    form = GalleryForm(instance=gal)
    return render(request, 'galleryedit.html', {'form': form})

def GalleryDelete(request,id):
    gal = get_object_or_404(GalleryModel, id=id)
    gal.delete()
    return redirect('galleryadmindisplay')

def FacilitiesaddView(request):
    if request.method=='POST':
        form = FacilitiesForm(request.POST)
        if form.is_valid():
            form.save()
    form=FacilitiesForm()
    return render(request,'facilitiesadminadd.html',{'form':form})

def FacilitiesdisplayView(request):
    fac = FacilitiesModel.objects.all()
    return render(request, 'facilitiesadmindisplay.html', {'fac': fac})

def FacilitiesEdit(request,id):
    fac = get_object_or_404(FacilitiesModel, id=id)
    if request.method == 'POST':
        form = FacilitiesForm(request.POST, instance=fac)
        if form.is_valid():
            form.save()
            return redirect('facilitiesadmindisplay')
    form = FacilitiesForm(instance=fac)
    return render(request, 'facilitiesedit.html', {'form': form})

def FacilitiesDelete(request,id):
    fac = get_object_or_404(FacilitiesModel, id=id)
    fac.delete()
    return redirect('facilitiesadmindisplay')

def DoctorsAdd(request):
    if request.method=='POST':
        form=DoctorsForm(request.POST)
        if form.is_valid():
            form.save()
    form=DoctorsForm()
    return render(request,'doctorsadd.html',{'form':form})

def DoctorsDisplay(request):
    doc=DoctorsModel.objects.all()
    return render(request,'doctorsdisplay.html',{'doc':doc})

def DoctorDetails(request,id):
    doc=get_object_or_404(DoctorsModel,id=id)
    return render(request,'doctordetails.html',{'doc':doc})

def DoctorsSingleDisplay(request,id):
    doc=DoctorsModel.objects.get(id=id)
    return render(request,'doctorssingleview.html',{'doc':doc})

def DoctorsEdit(request,id):
    doctor=get_object_or_404(DoctorsModel,id=id)
    if request.method == 'POST':
        form = DoctorsForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctorsdisplay')
    form = DoctorsForm(instance=doctor)
    return render(request, 'doctorsedit.html', {'form': form})

def DoctorsDelete(request,id):
    doc = get_object_or_404(DoctorsModel, id=id)
    doc.delete()
    return redirect('doctorsdisplay')

def Bookingadd(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm()
    return render(request,'bookingadd.html',{'form':form})

def BookingDisplay(request):
    book=BookingModel.objects.all()
    return render(request,'bookingdisplay.html',{'book':book})

def BookingEdit(request,id):
    book=get_object_or_404(BookingModel,id=id)
    if request.method=='POST':
        form=BookingForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('bookingdisplay')
    form=BookingForm(instance=book)
    return render(request,'bookingedit.html',{'form':form})

def BookingDelete(request,id):
    book = get_object_or_404(BookingModel, id=id)
    book.delete()
    return redirect('bookingdisplay')

def BookingSingleDisplay(request,id):
    book=BookingModel.objects.get(id=id)
    return render(request,'bookingsingleview.html',{'book':book})

def Careersadd(request):
    if request.method=='POST':
        form=CareersForm(request.POST)
        if form.is_valid():
            form.save()
    form=CareersForm()
    return render(request,'careersadd.html',{'form':form})

def CareersDisplay(request):
    car=CareersModel.objects.all()
    return render(request,'careersdisplay.html',{'car':car})

def CareersEdit(request,id):
    career = get_object_or_404(CareersModel, id=id)
    if request.method == 'POST':
        form = CareersForm(request.POST, instance=career)
        if form.is_valid():
            form.save()
            return redirect('careersdisplay')
    form = CareersForm(instance=career)
    return render(request, 'careersedit.html', {'form': form})

def CareersDelete(request,id):
    career = get_object_or_404(CareersModel, id=id)
    career.delete()
    return redirect('careersdisplay')

def CareersSingleDisplay(request,id):
    car=CareersModel.objects.get(id=id)
    return render(request,'careersingleview.html',{'car':car})

def CareerDetails(request,id):
    car=get_object_or_404(CareersModel,id=id)
    return render(request,'careerdetails.html',{'car':car})

def register_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful.You can now log in")
            return redirect('login')
        else:
            messages.error(request,"Registration failed.Please correct the errors below")
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/admin')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def index(request):
 return render(request, "index.html")  # Load the frontend page

def ajaxview(request):
 return render(request, "ajax.html")  # Load the frontend page

def get_data(request):
    """Fetches all Person data and returns JSON response"""
    persons = Person.objects.values("id", "name","email")
    print(list(persons)) # Convert QuerySet to a list of dictionaries
    return JsonResponse(list(persons), safe=False)


