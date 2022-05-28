from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import stu_reg_frm
from .models import stu_info
# Create your views here.
def indexPage(request):
    if request.method == "POST":
        form = stu_reg_frm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mycrudApp')      
    else:
        form = stu_reg_frm()
    all_data = stu_info.objects.all()
    return render(request, 'mycrudApp/add_show.html',{'form':form,'data':all_data})

def deleteData(request, id):
    if request.method =="POST":
        pi = stu_info.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/mycrudApp')

def updateData(request, id):
    if request.method == "POST":
        data = stu_info.objects.get(id=id)
        form = stu_reg_frm(request.POST,instance=data)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/mycrudApp')    
    else:
        data = stu_info.objects.get(id=id)
        form = stu_reg_frm(instance=data)
    return render(request, "mycrudApp/update.html",{'form': form})
    