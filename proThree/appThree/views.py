from django.shortcuts import render
from django import forms
from appThree.models import User
from appThree.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'appThree/index.html')

def users(request):
    user_list = User.objects.order_by('firstName')
    user_dict = {'user_records':user_list}
    return render(request,'appThree/user.html', context = user_dict)

def newuser(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return users(request)
        else:
            print("Error in Form")
    return render(request,'appThree/new_user.html',{'form':form})
