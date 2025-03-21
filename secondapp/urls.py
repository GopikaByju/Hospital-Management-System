from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('',views.homeview,name='homepage'),
    path('contactpage',views.contactview,name='contactpage'),
    path('aboutpage',views.aboutview,name='aboutpage'),
    path('departmentpage', views.departmentsview, name='departmentpage'),


    path('doctorspage',views.doctorsview,name='doctorspage'),
    path('bookingpage',views.bookingview,name='bookingpage'),
    path('bookingadd',views.Bookingadd,name='bookingadd'),
    path('bookingdisplay',views.BookingDisplay,name='bookingdisplay'),
    path('bookingedit/<int:id>/',views.BookingEdit,name='bookingedit'),
    path('bookingdelete/<int:id>/',views.BookingDelete,name='bookingdelete'),
    path('bookingsingleview/<int:id>/',views.BookingSingleDisplay,name='bookingsingleview'),

    path('gallerypage',views.galleryview,name='gallerypage'),
    path('facilitiespage',views.facilitiesview,name='facilitiespage'),
    path('deptadminadd',views.DepartmentView,name='deptadminadd'),
    path('deptdetails/<int:id>/',views.DepartmentDetailsView,name='deptdetails'),
    path('deptsingleview/<int:id>/',views.DepartmentSingleDisplay,name='deptsingleview'),
    path('deptadmindisplay',views.DepartmentDisplayView,name='deptadmindisplay'),
    path('deptadminedit/<int:id>/',views.DepartmentEdit,name='deptadminedit'),
    path('deptdelete/<int:id>/',views.DepartmentDelete,name='deptdelete'),
    path('galleryadminadd',views.GalleryaddView,name='galleryadminadd'),
    path('galleryadmindisplay',views.GallerydisplayView,name='galleryadmindisplay'),
    path('galleryadminedit/<int:id>/',views.GalleryEdit,name='galleryadminedit'),
    path('galleryadmindelete/<int:id>/',views.GalleryDelete,name='galleryadmindelete'),
    path('facilitiesadminadd',views.FacilitiesaddView,name='facilitiesadminadd'),
    path('facilitiesadmindisplay',views.FacilitiesdisplayView,name='facilitiesadmindisplay'),
    path('facilitiesadminedit/<int:id>/',views.FacilitiesEdit,name='facilitiesadminedit'),
    path('facilitiesadmindelete/<int:id>/',views.FacilitiesDelete,name='facilitiesadmindelete'),
    path('doctorsadd',views.DoctorsAdd,name='doctorsadd'),
    path('doctorsdisplay',views.DoctorsDisplay,name='doctorsdisplay'),
    path('doctordetails/<int:id>/',views.DoctorDetails,name='doctordetails'),
    path('doctorsedit/<int:id>/',views.DoctorsEdit,name='doctorsedit'),
    path('doctorsdelete/<int:id>/',views.DoctorsDelete,name='doctorsdelete'),
    path('doctorssingleview/<int:id>/',views.DoctorsSingleDisplay,name='doctorssingleview'),
    path('careers', views.CareersView, name='careers'),
    path('careersadd', views.Careersadd, name='careersadd'),
    path('careersdisplay', views.CareersDisplay, name='careersdisplay'),
    path('careersedit/<int:id>/', views.CareersEdit, name='careersedit'),
    path('careersdelete/<int:id>/', views.CareersDelete, name='careersdelete'),
    path('careersingleview/<int:id>/', views.CareersSingleDisplay, name='careersingleview'),
    path('careerdetails/<int:id>/', views.CareerDetails, name='careerdetails'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('ajax', views.ajaxview, name='ajax'),
    path('index', views.index, name="index"),  # Load frontend page
    path("get-data/", views.get_data, name="get_data"),  # AJAX endpoint


]
