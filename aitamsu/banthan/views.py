from django.shortcuts import render
from .forms import bffForm
#from .services.openai_service import banthanchat


def home(request):
    answers = None
    if request.method == 'POST':
        form = bffForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            questions = form.cleaned_data['questions']
            answers = banthanchat(name, description, questions, answers)
    else:
        form = bffForm()
    return render(request, 'home.html', {'form': form, 'answers': answers})