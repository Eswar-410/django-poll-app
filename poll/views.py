from django.shortcuts import render, redirect
from .forms import ValidForm
from .models import CreateForm

# Create your views here.


def index(request):

    form_sets = CreateForm.objects.all()
    return render(request, 'index.html', {'form_sets': form_sets})


def create_form(request):
    form = ValidForm()
    return render(request, 'create.html', {'form': form})


def load_form(request):
    if request.method == 'POST':
        form = ValidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ValidForm()

    form_sets = CreateForm.objects.all()
    return render(request, 'index.html', {'form_sets': form_sets})


def vote(request, pk):
    form_set = CreateForm.objects.get(pk=pk)
    if request.method=='POST':
        selected_option=request.POST.get('choice')

        if selected_option=='option_One':
            form_set.option_one_count+=1
        elif selected_option=='option_Two':
            form_set.option_two_count+=1
        elif selected_option=='option_Three':
            form_set.option_three_count+=1

        form_set.save()
        return redirect('index')

    return render(request, 'vote.html', {'form_set': form_set})


def results(request):
    form_sets = CreateForm.objects.all()
    return render(request, 'results.html', {'form_sets': form_sets})
