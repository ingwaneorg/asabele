from django.shortcuts import render, redirect
from .models import LearnerStatus
from .forms import LearnerStatusForm


def learner_view(request, room_code):
    print(f"learner_view: {room_code}")
    template_name = 'learner.html'
    form = LearnerStatusForm(request.POST or None)  # Keeps submitted data

    if not form.is_valid():
        print("Form errors:", form.errors)  # Print validation errors for debugging

    if request.method == "POST":
        print(f"POST data: {request.POST}")  # Check what data is being submitted        
        if form.is_valid():
            print("-- form is valid")
            learner_id = form.cleaned_data['learner_id']
            first_name = form.cleaned_data['first_name']
            room_code = form.cleaned_data['room_code'].lower()  # Enforce lowercase
            status_value = form.cleaned_data['status']
            submitted_text = form.cleaned_data['answer']

            # Update if learner_id exists, otherwise create a new record
            learner_status, created = LearnerStatus.objects.update_or_create(
                learner_id=learner_id,
                defaults={
                    'first_name': first_name, 
                    'room_code': room_code, 
                    'status': status_value, 
                    'answer': submitted_text
                }
            )

            print(f"Saved: {learner_status}, Created: {created}")  # Debugging output

            # Form stays filled with submitted data after refresh
            return render(request, template_name, {'form': form, 'success': "Status updated!"})

    return render(request, template_name, {'form': form})


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

