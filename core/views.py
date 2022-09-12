from django.shortcuts import render, redirect
from .forms import RegexForm

# Create your views here.
def index(request):
    if request.method == 'POST' and 'regex_submit' in request.POST:
        print('This works')
        return redirect('index')
        

    else:
        form = RegexForm()
        
        context = {
            'form': form
        }

        return render(request, 'index.html', context)