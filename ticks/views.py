import re

from django.conf import settings
from django.http import Http404
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render

from django.db.models import F

from .models import LearnerStatus
from .forms import LearnerStatusForm

# Parameters
last_seen = timezone.now()-timedelta(hours=4)


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
            form = LearnerStatusForm(initial={'first_name': first_name})  # Reset form

    context = {
        'form': form,
        'room_code': room_code,
    }
    return render(request, template_name, context)


def tutor_view(request, room_code):
    template_name = 'tutor.html'
    room_code = validate_room_code(room_code)

    # Get url for learners
    url = request.build_absolute_uri('/')+room_code.lower()

    # Get learner records from the database for this room
    learners = LearnerStatus.objects.filter(
        room_code=room_code,
        timestamp__gte=last_seen
        )

    context = {
        'learners': learners,
        'room_code': room_code,
        'url': url,
    }
    return render(request, template_name, context)


def poll_view(request, room_code):
    template_name = 'poll.html'
    room_code = validate_room_code(room_code)

    # Get learner records from the database for this room
    learner_count = LearnerStatus.objects.filter(
        room_code=room_code,
        timestamp__gte=last_seen
        ).count()

    # Query learners and group by status, counting each status
    learners_by_status = LearnerStatus.objects.filter(
        room_code=room_code,
        timestamp__gte=last_seen
        ).exclude(status='clear'
        ).values('status'
        ).annotate(names=F('first_name')
        ).order_by('status')

    # Group by status
    status_counts = {}
    for learner in learners_by_status:
        if learner['status'] not in status_counts:
            status_counts[learner['status']] = []
        status_counts[learner['status']].append(learner['names']) # names comes from the annotation

    # Get the maximum count of learners in any status
    max_count = max(len(learners) for learners in status_counts.values())

    context = {
        'status_counts': status_counts,
        'room_code': room_code,
        'learner_count': learner_count,
        'max_count': max_count,
    }
    return render(request, template_name, context)


# Static Views
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

