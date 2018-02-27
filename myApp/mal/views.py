from django.shortcuts import render
from django.http import HttpResponse
from mal.forms import NewAnimeForm
from mal.models import Topic
from mal.models import Animes

def index(request):
    return HttpResponse("Project Index.")

def app_index(request):
    return HttpResponse('M.A.L Index.')

def helper(request):
    return render(request, 'mal/home.html')

def animes(request):
    style = Topic.objects.order_by('top_name')
    animes = Animes.objects.order_by('name')
    

    dict = {
        'style':style,
        'animes':animes,
    }

    return render(request, 'mal/animes.html', context=dict)

def form(request):
    form = NewAnimeForm()

    if request.method == 'POST':
        form = NewAnimeForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return animes(request)
        else:
            print("¡ERROR!")
    return render(request, 'mal/form.html', {'form':form})


    
