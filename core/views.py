from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import SignUpForm
from django.contrib.auth import login,logout
# Create your views here.
class FrontPage(View):
    def get(self,request):
        return render(request,'frontpage.html')
    
 
class SignUp(View):
    def get(self,request):
        form=SignUpForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request):
        form_data=SignUpForm(data=request.POST)
        if form_data.is_valid():
            user=form_data.save()
            login(request,user)
            return redirect('frontpage')
        else:
            return render(request,'signup.html',{'form':form_data})