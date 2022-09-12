from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegexForm
import re

# Create your views here.
def index(request):
    if request.method == 'POST' and 'regex_submit' in request.POST:
        expression = request.POST['expression']
        text = request.POST['text']

        pattern = re.compile(expression)

        matches = pattern.finditer(text)

        for match in matches:
            messages.info(request, match.group(0))
            return redirect('index')        

    else:
        form = RegexForm()
        
        context = {
            'form': form
        }

        return render(request, 'index.html', context)