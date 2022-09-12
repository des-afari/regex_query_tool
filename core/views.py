from django.shortcuts import render
from .forms import RegexForm

# Create your views here.
def index(request):
    form = RegexForm()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)