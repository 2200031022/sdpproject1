from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('/hello',hello,name='hello'),
    path('',newhomepage,name='homepage'),
    path('travelpackage',travelpackage,name='travelpackage'),
    path('print_to_console/',print_to_console,name="print_to_console"),
    path('print1/',print1,name="print1"),
    path('randomcall/',randomcall,name='randomcall'),
    path('randomlogic/',randomlogic,name='randomlogic'),
    path('get_date/',get_date,name='get_date'),
    path('myregisterpage/',myregisterpage,name='myregisterpage'),
    path('registerloginfunction',registerloginfunction,name='registerloginfunction'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),

]