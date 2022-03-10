from django.urls import path
from barberapp import views

urlpatterns =[

path("",views.index),
path("about/",views.about),
path("codes/",views.codes),
path("contact/",views.contact),
path("gallery/",views.gallery),
path("icons/",views.icons),
path("single/",views.single),
path("barber/",views.barber),
path("userreg/",views.userreg),
path("userlog/",views.userlog),
path("barberlog/",views.barberlog),
path("userdata/",views.userdata),
path("barberdata/",views.barberdata),
path("userlogin/",views.userlogin),
path("barberlogin/",views.barberlogin),
path("logout/",views.logout),
path("booking/",views.booking),
path("table/",views.table),
path("approve/",views.approve),
path("cancel/",views.cancel),
path("adminindex/",views.adminindex),
path("cards/",views.cards),
path("blocks/",views.blocks),
path("carousels/",views.carousels),
path("forms/",views.forms),
path("people/",views.people),
path("pricing/",views.pricing),
path("adminlogin/",views.adminlogin),
path("adminlog/",views.adminlog),
path("usertable/",views.usertable),
path("barbertable/",views.barbertable),
path("bookingtable/",views.bookingtable),
path("addservices/",views.addservices),
path("addservice/",views.addservice),
path("barberorder/",views.barberorder),
path("mybooking/",views.mybookings),
path("barberindex/",views.barberindex),
path("changepassword/",views.changepassword),
path("userdetials/",views.userdetials),
path("barberbooking/",views.barberbooking),
















]