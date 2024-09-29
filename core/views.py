from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/core.html', {})

def profile(request):
    context = {
        'fav_shows' : ["Lost", "Mr.Robot", "Aquí no hay quien viva"]
    }
    return render(request, 'core/profile.html', context)