from django.urls import path
from . import views

urlpatterns = [
    path("hotel-owner/",views.hotel_owner,name="hotel_owner"),
    path("delivery-partner/",views.delivery_partner,name="delivery_partner"),
    path("supplier/",views.supplier,name="supplier"),
    path("captain/",views.captain,name="captain"),
    path("chef/",views.chef,name="chef"),
    path("receptionist/",views.receptionist,name="receptionist"),
    path("login/",views.login_view,name="login"),

]