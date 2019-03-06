from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import Movie

# Create your views here.
def movie_home_view(request):
    return render(request, 'testapp/home.html')

def add_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return movie_home_view(request)
    return render(request, 'testapp/add.html',{'form':form})

def list_view(request):
    form=Movie.objects.all()
    return render(request, 'testapp/list.html',{'form':form})




