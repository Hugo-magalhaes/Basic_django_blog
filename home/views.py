from django.shortcuts import render

# Create your views here.
context = {
    'text': 'Bem-vindo a Home',
    'title': 'Home do '
}


def home(request):
    return render(request,
                  'home/index.html',
                  context)
