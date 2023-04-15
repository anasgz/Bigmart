from django.urls import path
from frontend import views

urlpatterns=[
    path('homepage/', views.homepage, name="homepage"),
    path('aboutuspage/', views.aboutuspage, name="aboutuspage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('categorydisplaypage/', views.categorydisplaypage, name="categorydisplaypage"),
    path('discategory/<itemcatg>', views.discategory, name="discategory"),
    path('prodetails/<int:dataid>', views.prodetails, name="prodetails"),
    path('registrationpage/', views.registrationpage, name="registrationpage"),
    path('saveregistration/', views.saveregistration, name="saveregistration"),
    path('displayloginpage/', views.displayloginpage, name="displayloginpage"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('customerlogout/', views.customerlogout, name="customerlogout"),
    path('savecontact/', views.savecontact, name="savecontact"),

]