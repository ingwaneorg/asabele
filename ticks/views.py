from django.shortcuts import render, redirect

from .models import UserChoice
from .forms import ChoiceForm

def choice_view(request):
    if request.method == "POST":
        choice_value = request.POST.get('choice')
        submitted_text = request.POST.get('user_input')
        print(choice_value, submitted_text)
        if choice_value in ['A', 'B']:  # Ensure only A or B is stored
            UserChoice.objects.create(choice=choice_value)
    
    form = ChoiceForm()  # Create a new form for the next selection
    return render(request, 'choice_form.html', {'form': form})


# Ticks Views
def introPage(request):
    template_name = 'intro.html'
    context = {
    }
    return render(request, template_name, context)

def aboutPage(request):
    template_name = 'about.html'
    context = {
    }
    return render(request, template_name, context)

def browserCheck(request):
    template_name = 'browser-check.html'
    context = {
    }
    return render(request, template_name, context)

def learnerView(request, room_code):
    template_name = 'learner.html'
    context = {
    }
    return render(request, template_name, context)

