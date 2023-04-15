from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from backend.models import adminreg, categorydb, productdb, contactdb


# Create your views here.
def indexpage(req):
    return render(req,"index.html")
def addadminpage(req):
    return render(req,"addadmin.html")
def saveadminpage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mob = request.POST.get('mobile')
        user = request.POST.get('username')
        password = request.POST.get('password')
        img = request.FILES['image']
        obj = adminreg(NAME=na, EMAIL=em, MOBILE=mob, USERNAME=user, PASSWORD=password, IMAGE=img)
        obj.save()
        return redirect(addadminpage)

def displayadmin(req):
    data = adminreg.objects.all()
    return render(req,"displayadmin.html", {'data':data})
def editadminpage(req,dataid):
    data = adminreg.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html", {'data':data})


def updateadmin(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        mob = req.POST.get('mobile')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = adminreg.objects.get(id=dataid).IMAGE
        adminreg.objects.filter(id=dataid).update(NAME=na, EMAIL=email, MOBILE=mob, USERNAME=uname, PASSWORD=passwrd, IMAGE=file)
        return redirect(displayadmin)
def deleteadmin(req,dataid):
    data = adminreg.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)


def categorypage(req):
    return render(req,"category.html")
def savecategorypage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        dis = request.POST.get('discription')
        img = request.FILES['image']
        obj = categorydb(NAME=na, DISCRIPTION=dis, IMAGE=img)
        obj.save()
        return redirect(categorypage)

def displaycategorypage(req):
    data = categorydb.objects.all()
    return render(req,"displaycategory.html", {'data':data})

def editcategorypage(req,dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(req,"editcategory.html", {'data':data})
def updatecategorypage(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).IMAGE
        categorydb.objects.filter(id=dataid).update(NAME=na, DISCRIPTION=dis, IMAGE=file)
        return redirect(displaycategorypage)
def deletecategory(req,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategorypage)

def products(req):
    data = categorydb.objects.all()
    return render(req,"products.html", {'data':data})
def saveproducts(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pri = request.POST.get('price')
        qua = request.POST.get('quantity')
        dis = request.POST.get('discription')
        img = request.FILES['image']
        cat = request.POST.get('category')
        obj = productdb(NAME=na, PRICE=pri, QUANTITY=qua, DISCRIPTION=dis, CATEGORY=cat, IMAGE=img)
        obj.save()
        return redirect(products)
def displayproduct(req):
    data = productdb.objects.all()
    return render(req, "displayproduct.html", {'data': data})
def editproduct(req,dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    print(da)
    return render(req,"editproduct.html", {'datas':data,'da':da})
def updateproduct(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        pr = req.POST.get('price')
        qua = req.POST.get('quantity')
        dis = req.POST.get('discription')
        cat = req.POST.get('category')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).IMAGE
        productdb.objects.filter(id=dataid).update(NAME=na, PRICE=pr, QUANTITY=qua, DISCRIPTION=dis, CATEGORY=cat, IMAGE=file)
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def loginpage(req):
    return render(req,"loginpage.html")

def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(addadminpage)
        else:
            return redirect(addadminpage)

def logoutadmin(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def contactpageview(req):
    data=contactdb.objects.all()
    return render(req,"contactview.html",{'data':data})
def deletecontact(req,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(contactpageview)
