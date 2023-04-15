from django.shortcuts import render, redirect

from backend.models import categorydb, productdb, contactdb
from frontend.models import registrationdb
from django.contrib import messages


# Create your views here.
def homepage(req):
    data = categorydb.objects.all()
    return render(req,"home.html",{'data':data})
def aboutuspage(req):
    return render(req,"aboutus.html")
def contactpage(req):
    return render(req,"contact.html")
def categorydisplaypage(req):
    return render(req,"categorydisplay.html")
def discategory(req,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(CATEGORY=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(req,"categorydisplay.html",context)


def prodetails(request,dataid):
    data=productdb.objects.get(id=dataid)
    return render(request,"productdisplay.html",{'dat':data})

def registrationpage(req):
    return render(req,"registration.html")
def saveregistration(req):
    if req.method == "POST":
        na = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('pass1')
        cmfpass = req.POST.get('pass2')
        obj = registrationdb(Name=na, Email=email, Password=password, Conformpassword=cmfpass)
        obj.save()
        return redirect(registrationpage)
def displayloginpage(req):
    return render(req,"registration.html")

def customerlogin(req):
    if req.method=='POST':
        username_r=req.POST.get("username1")
        password_r=req.POST.get("password1")
        if registrationdb.objects.filter(Name=username_r,Password=password_r).exists():
            req.session['username1']=username_r
            req.session['password1']=password_r
            messages.success(req,"login successfully")

            return redirect(homepage)
        else:
            messages.error(req,"error")
            return render(req,"registration.html",{'msg':"sorry....invalid username or password"})
def customerlogout(req):
    del req.session['username1']
    del req.session['password1']
    return redirect(registrationpage)

def savecontact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        su = request.POST.get('subject')
        me = request.POST.get('message')
        obj = contactdb(NAME=na, EMAIL=em, SUBJECT=su, MESSAGE=me)
        obj.save()
        return redirect(contactpage)

