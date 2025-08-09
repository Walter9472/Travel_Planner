from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from travello.models import Destination

def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dest':dests})

@login_required(login_url='login')
def destination(request,dest_id):
    dest = get_object_or_404(Destination,pk=dest_id)
    return render(request,'destination.html',{'dest':dest})