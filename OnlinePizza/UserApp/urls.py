from django.urls import path 
from .import views

urlpatterns = [ 
    path('',views.homepage),
    path('login',views.login),
    path('signup',views.signup),
    path('showpizza/<id>',views.showpizza),
    path('viewdetails/<id>',views.viewdetails),
    path('signout',views.signout),
    path('addtocart',views.addtocart),
    path('showcartitems',views.showcartitems),
    path('makepayment',views.makepayment),
    path('removeitem',views.removeitem),
    path('contact',views.contact),
]