from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import Computer
from .forms import ComputerForm, SelectComputer
from . import wol

# Create your views here.

def select_computer(request):
    if request.method == 'POST':
        form = SelectComputer(request.POST)
        if form.is_valid():
            wol.send_wol(form.data['computers'])
            return redirect('wol_results',form.data['computers'])
        return render(request, 'select_computer.html', {'form':form})
    form = SelectComputer()
    return render(request, 'select_computer.html', {'form':form})

def add_computer(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.save()
            return redirect('select_computer')  
        return render(request, 'add_computer.html', {'form':form})    
    form = ComputerForm()
    return render(request, 'add_computer.html', {'form':form})

def wol_results(request, computer_pk):
    computer = get_object_or_404(Computer, pk=computer_pk)
    return render(request, 'wol_results.html', {'computer':computer})

def ping_computer(request, computer_pk):
    computer = get_object_or_404(Computer, pk=computer_pk)
    result = wol.send_ping(computer.pk)
    data = {
        'ping_code': result
    }
    return JsonResponse(data)

