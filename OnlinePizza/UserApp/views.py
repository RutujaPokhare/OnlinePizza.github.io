from django.shortcuts import render,redirect
from AdminApp.models import Category ,Product ,UserInfo ,PaymentMaster 
from UserApp.models import MyCart ,OrderMaster
from datetime import datetime
from django.contrib import messages
# Create your views here.

def homepage(request):
    #fetch all records
    cats = Category.objects.all()
    pizza = Product.objects.all()
    return render(request,"homepage.html",{"cats":cats,"pizza":pizza})

def login(request):
    if(request.method == "GET"):
      return render(request,"login.html",{})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        try:
            user = UserInfo.objects.get(username = uname,password = password)
            messages.success(request,"Login Successful")
            request.session["uname"]=uname
            return redirect(homepage)
        except:
            messages.success(request,"Invalid Login")
            return redirect(login)
        else:
            return redirect(homepage)

def signup(request):
    if(request.method == "GET"):
        return render(request,"signup.html",{})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = UserInfo(uname,password,email)
        user.save()
        messages.success(request,"Signed Up Successfully")
        return redirect(homepage)

def signout(request):
    request.session.clear()
    return redirect(homepage)

def showpizza(request,id):
    id = Category.objects.get(id=id)
    pizza = Product.objects.filter(cat = id)
    cats = Category.objects.all()
    return render (request,"homepage.html",{"cats":cats,"pizza":pizza})

    
def viewdetails(request,id):
    pizza = Product.objects.get(id = id)
    return render(request,"viewdetails.html",{"pizza":pizza}) 

def addtocart(request):
    if(request.method=="POST"):
        if("uname" in request.session):
            pizzaid = request.POST["pizzaid"]
            user = request.session["uname"]
            quantity = request.POST["quantity"]
            pizza = Product.objects.get(id=pizzaid)
            user = UserInfo.objects.get(username = user)
            try:
                cart = MyCart.objects.get(pizza= pizza,user = user)
            except:
                cart = MyCart()
                cart.user = user
                cart.pizza = pizza
                cart.quantity = quantity
                cart.save()
            else:
                pass
            return redirect(homepage)
        else:
            return redirect(login)

def showcartitems(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(username=uname)
    if(request.method == "GET"):
        
        cartitems = MyCart.objects.filter(user=user)
        total = 0
        for item in cartitems:
            total += item.quantity * item.pizza.price
        request.session["total"] = total
        return render(request,"showcartitems.html",{"items":cartitems})
    else:
        
        id = request.POST["pizzaid"]
        pizza = Product.objects.get(id=id)
        item = MyCart.objects.get(user=user,cake=cake)
        quantity = request.POST["quantity"]
        item.quantity = quantity
        item.save() #update
        return redirect(showcartitems)

def removeitem(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(username=uname)
    id = request.POST["pizzaid"]
    pizza = Product.objects.get(id = id)
    item = MyCart.objects.get(user = user,pizza=pizza)
    item.delete()
    return redirect(showcartitems)


def makepayment(request):
    if(request.method == "GET"):
        return render(request,"makepayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = PaymentMaster.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(makepayment)
        else:
            owner = PaymentMaster.objects.get(cardno='111',cvv='222',expiry='12/25')
            owner.balance += request.session["total"]
            buyer.balance -= request.session["total"]
            owner.save()
            buyer.save()
            
            #Delete all items from cart
            uname = request.session["uname"]
            user = UserInfo.objects.get(username=uname)
            order = OrderMaster()
            order.user = user
            order.amount = request.session["total"]
            details = ""
            items = MyCart.objects.filter(user = user)
            for item in items:
                details +=(item.pizza.pname)+","
                item.delete()
            order.details = details
            order.save()
            return redirect(homepage)


def contact(request):
    return render(request,"contact.html",{})
    