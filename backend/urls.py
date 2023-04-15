from django.urls import path
from backend import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addadminpage/', views.addadminpage, name="addadminpage"),
    path('saveadminpage/',views.saveadminpage,name="saveadminpage"),
    path('displayadmin/', views.displayadmin, name="displayadmin"),
    path('editadminpage/<int:dataid>/', views.editadminpage, name="editadminpage"),
    path('updateadmin/<int:dataid>/', views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),

    path('categorypage/',views.categorypage,name="categorypage"),
    path('savecategorypage/', views.savecategorypage, name="savecategorypage"),
    path('displaycategorypage/', views.displaycategorypage, name="displaycategorypage"),
    path('editcategorypage/<int:dataid>/', views.editcategorypage, name="editcategorypage"),
    path('updatecategorypage/<int:dataid>/', views.updatecategorypage, name="updatecategorypage"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),

    path('products/', views.products, name="products"),
    path('saveproducts/', views.saveproducts, name="saveproducts"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),

    path('logoutadmin/', views.logoutadmin, name="logoutadmin"),

    path('contactpageview/', views.contactpageview, name="contactpageview"),
    path('deletecontact/<int:dataid>/', views.deletecontact, name="deletecontact")

]