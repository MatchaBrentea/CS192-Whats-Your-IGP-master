# MIT License

# Copyright (c) Justin James Gonzales, Martin Thomas Saliba, Brent Zaguirre

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# “This is a course requirement for CS 192 Software Engineering II under the supervision of 
# Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, 
# University of the Philippines, Diliman for the AY 2015-2016”.

# =================================================================================

# CODE HISTORY:
# <1/26/2019>
# 1) Code initialization
# 2) License
# 3) Main Functionality (Backend):
#   a.  url calls

# ---------------------------------------------------------------------------------

# <2/08/2019>
# 1)  Creation Date
# 2)  Development Group
# 3)  Client Group
# 4)  Purpose
# 5)  Methods

# =================================================================================   

# Creation Date: <1/26/2019>

# =================================================================================

# Development Group: What's Your IGP

# =================================================================================

# Client Group: What's Your IGP

# =================================================================================

# Purpose:
# > The purpose of the project: "What's Your IGP," is for the fufillment of the course: "CS 192." The project
# aims to centralize the Income Generated Projects (IGP's) online information of all existing organizations
# associated with UP Diliman. It's objective is to offer convenience for both sellers and customers of IGP
# to sell and gather information online.  

# =================================================================================
from django.conf.urls import url,include

#from mysite.core import views as core_views
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings
from .views import (
	IGPListView,  
	IGPCreateView,
	IGPDeleteView,
	IGPUpdateView,
	
	ORGListView,
	ORGDetailView,
	ORGCreateView,
	ORGUpdateView,
	ORGDeleteView
	)
from . import views

urlpatterns = [
	#path('', views.signup, name="signup"),
    #path('', views.login_view, name='home'),
    #path('orgs/<int:pk>/', BuyerIGP.as_view(), name='buyer_orgigps_detail'),
    path('seller/orgs/<int:pk>/', views.SellerIGP, name='seller_orgigps_detail'),
    path('buyer/orgs/<int:pk>/', views.BuyerIGP, name='buyer_orgigps_detail'),
    path('', views.home, name='app-home'),
    path('igps/new/', IGPCreateView.as_view(), name='igp-create'),
    path('orgs/new/', ORGCreateView.as_view(), name='org-create'),
    path('igps/<int:pk>/delete/', IGPDeleteView.as_view(), name='igp-delete'),
    path('igps/<int:pk>/update/', IGPUpdateView.as_view(), name='igp-update'),
    path('orgs/<int:pk>/delete/', ORGDeleteView.as_view(), name='org-delete'),
    path('orgs/<int:pk>/update/', ORGUpdateView.as_view(), name='org-update'),
    path('orgs/<int:pk>/', ORGDetailView.as_view(), name='orgigps_detail'),
    path('signup/', views.signup, name="signup"),
    path('memsignup/', views.memsignup, name="memsignup"),
    path('igps/', IGPListView.as_view(), name='app-igps'),
    path('orgs/', ORGListView.as_view(), name='app-orgs'),
    path('buyer/igps/',views.list_igp,name='list_igp'),
    path('buyer/orgs/',views.list_org,name='list_org'),
    path('buyer/profile/',views.profile,name='buyer_profile'),
    path('org/profile/',views.orgprofile,name='org_profile'),
    path('create/igp/',views.createigp,name='createigp'),
    path('org/igp/',views.my_igp,name='my_igp'),
    path('igp/detail/<int:pk>/',views.igpdetail,name='igpdetail'),
    path('seller/igp/detail/<int:pk>/',views.seller_igpdetail,name='seller_igpdetail'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)