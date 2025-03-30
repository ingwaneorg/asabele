import re

from django.conf import settings
from django.http import Http404

from django.shortcuts import render
from .models import LearnerStatus
from .forms import LearnerStatusForm


def validate_room_code(room_code):
    """Ensures the room code is alphanumeric and converts it to uppercase."""
    if not re.match(r'^[A-Za-z0-9]+$', room_code):  
        raise Http404("Room can only consist of letters and numbers.")

    if len(room_code) < 2 or len(room_code) > 10:  
        raise Http404(f"Room length must be <= 10 [{len(room_code)}]")

    return room_code.upper()  # Return the uppercase version


def learner_view(request, room_code):
    template_name = 'learner.html'
    form = LearnerStatusForm(request.POST)

    # Make sure that the room code is valid
    room_code = validate_room_code(room_code)
    if request.method == "POST":
        print(f"POST data: {request.POST}")  # Check what data is being submitted

        if not form.is_valid():
            return render(request, template_name, {'form': form})

        # Form is valid so save the record
        learner_id = form.cleaned_data['learner_id']
        first_name = form.cleaned_data['first_name']
        status = form.cleaned_data['status']
        answer = form.cleaned_data['answer']

        # for testing change learner_id so that can have multiple users in one browser
        if settings.DEBUG:
            learner_id = first_name+":"+learner_id
            print(learner_id)

        # Update if learner_id exists, otherwise create a new record
        learner_status, created = LearnerStatus.objects.update_or_create(
            learner_id=learner_id,
            defaults={
                'first_name': first_name, 
                'room_code': room_code, 
                'status': status, 
                'answer': answer
            }
        )

        # if clear pressed keep name only
        if status == "clear":
            print(f"\ncleared {first_name}\n")
            form = LearnerStatusForm(initial={'first_name': first_name})  # Reset form


    context = {
        'form': form,
        'room_code': room_code
    }
    return render(request, template_name, context)


# Ticks Views
def home_page(request):
    template_name = 'home.html'
    context = {
    }
    return render(request, template_name, context)

def about_page(request):
    template_name = 'about.html'
    context = {
    }
    return render(request, template_name, context)

def browser_check(request):
    template_name = 'browser-check.html'
    context = {
    }
    return render(request, template_name, context)

