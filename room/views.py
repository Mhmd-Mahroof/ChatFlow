from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Room,Messages
from django.views.generic import View
# Create your views here.

method_decorator(login_required,name='dispatch')
class Rooms(View):
    def get(self,request):
        rooms=Room.objects.all()
        return render(request,'rooms.html',{'room':rooms})
    
method_decorator(login_required,name='dispatch')
class RoomView(View):
    def get(self,request,**kwargs):
        room=Room.objects.get(slug=kwargs['slug'])
        messages=Messages.objects.filter(room=room)[0:25]
        return render(request,'room2.html',{'room':room,'messages':messages})

