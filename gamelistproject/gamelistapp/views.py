from django.shortcuts import render,redirect
from gamelistapp.models import Games
from gamelistapp.forms import GameForm
# Create your views here.
def retrive_games(request):

    games=Games.objects.all()

    return render(request,'gamelistapp/index.html',{'games':games})


def add_games(request):

    form=GameForm()

    if request.method=='POST':
        form=GameForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/gamelistapp/list')
            

    return render(request,'gamelistapp/add.html',{'form':form})


def del_games(request,id):

    game=Games.objects.get(id=id)
    
    game.delete()

    return redirect('/gamelistapp/list')


def Update_games(request,id):

    game=Games.objects.get(id=id)
    print("Hi")
      
    if request.method=='POST':
        form=GameForm(request.POST,instance=game)
    
        if form.is_valid():
            form.save()
            return redirect('/gamelistapp/list')
            
    return render(request,'gamelistapp/update.html',{'game':game})