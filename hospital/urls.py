from django.urls import path
from .import views
urlpatterns = [
    path('',views.login,name='login'),
    path('userlogin',views.user_login,name='userlogin'),
    path('logout',views.logout_view),
    path('accounts/sign_up/',views.sign_up,name="signup"),
    path('passwordreset',views.resetPassword,name="passwordreset"),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('complaints',views.mycomplaints,name="complaints"),
    path('department',views.mydepartment,name="department"),
    path('doctors',views.mydoctors,name="doctors"),
    path('ourhospital',views.myhospital,name="ourhospital"),
    path('aidoctor',views.myaidoctor,name="aidoctor"),
    path('payment',views.mypayment,name="payment"),
    path('virtualdoctor',views.myvirtualdoctor,name="virtualdoctor"),
    path('booking',views.mybooking,name="booking"),

]