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
from .models import ORG,IGP
from . import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
CHOICES=[('select1','Seller'),
         ('select2','Buyer')]

class SignUpForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    college = forms.CharField(max_length=30, required=True, help_text='Required.')
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    mobile_number = forms.CharField(required=True, label="Contact no", widget=forms.TextInput(
        attrs={'class': 'form-control form-group',
               'placeholder': '+639999999999'})
        )
    class Meta:
        model = User
        fields = ('username','mobile_number','user_type','college', 'password1', 'password2' )

class Orgform(forms.ModelForm):
    name = forms.CharField(required=True, label="Organization", widget=forms.TextInput)
    description = forms.CharField(required=True, label="Description", widget=forms.TextInput)
    location = forms.CharField(required=True, label="Location", widget=forms.TextInput)
    mobile_number = forms.CharField(required=True, label="Contact no", widget=forms.TextInput(attrs={'class': 'form-control form-group','placeholder': '+639999999999'}))
    class Meta:
      model=ORG
      fields=('name','description','location','mobile_number')

class Igpform(forms.ModelForm):
    item = forms.CharField(required=True, label="item", widget=forms.TextInput)
    itype = forms.CharField(required=True, label="itype", widget=forms.TextInput)
    price = forms.CharField(required=True, label="price", widget=forms.TextInput)
    class Meta:
      model=IGP
      fields=('item','itype','price')