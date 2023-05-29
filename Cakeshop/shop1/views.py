from django.shortcuts import render, redirect
from .forms import CakeshopForm
from .models import Cakeshop
from django.contrib.auth.decorators import login_required

# Create your views here.
def order_view(request):
    form = CakeshopForm
    if request.method == "POST":
        form = CakeshopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details')
    template_name = "shop1/order.html"
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='login')
def details_view(request):
    data = Cakeshop.objects.all()
    context = {'data':data}
    template_name = 'shop1/details.html'
    return render(request, template_name, context)


def update_view(request, pk):
    data = Cakeshop.objects.get(id=pk)
    form = CakeshopForm(instance=data)
    if request.method == "POST":
        form = CakeshopForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('details')
    template_name = 'shop1/order.html'
    context = {'form': form}
    return render(request, template_name, context)

def delete_view(request, pk):
    data = Cakeshop.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('details')
    template_name = 'shop1/delete.html'
    context = {'data':data}
    return render(request,template_name ,context)