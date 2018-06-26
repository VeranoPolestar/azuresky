from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):

    context = {
        'title': 'AzureSky',
        'welcome': 'Welcome to AzureSky!',
    }
    return render(request, 'blog/index.html', context)
