from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Legend
def index(request):
    legends = Legend.objects.all()
    context = {'legends': legends}
    return render(request, 'legends/index.html', context)
def add(request):
    return render(request, 'legends/add.html')
def insert(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    legend = Legend(first_name=first_name, last_name=last_name, age=age)
    legend.save()
    return HttpResponseRedirect('/legends/')
def edit(request, legend_id):
    legend = get_object_or_404(Legend, pk=legend_id)
    context = {'legend': legend}
    return render(request, 'legends/edit.html', context)
def update(request, legend_id):
    legend = get_object_or_404(Legend, pk=legend_id)
    legend.first_name = request.POST.get('first_name')
    legend.last_name = request.POST.get('last_name')
    legend.age = request.POST.get('age')
    legend.save()
    return HttpResponseRedirect('/legends/')
def delete(request, legend_id):
    legend = get_object_or_404(Legend, pk=legend_id)
    legend.delete()
    return HttpResponseRedirect('/legends/')