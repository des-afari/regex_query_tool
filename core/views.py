from django.shortcuts import render
from .forms import RegexForm

# Create your views here.
def index(request):
    if request.method == 'POST' and 'regex_submit' in request.POST:
        form = RegexForm()

        if form.is_valid():
            pass

    else:
        form = RegexForm()
        
        context = {
            'form': form
        }

        return render(request, 'index.html', context)