from django.shortcuts import render, redirect, HttpResponse
from .models import Appointment
from datetime import datetime

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {})

def signupAction(request):
    if request.method == 'POST':
        output = ""
        first_name = request.POST.get('fname', "")  
        last_name = request.POST.get('lname', "")
        contact = request.POST.get('phno', "")
        password = request.POST.get('pass', "")
        location = request.POST.get('loc', "")
        state = request.POST.get('state', "")
        gender = request.POST.get('gender', "")
        dob = request.POST.get('dob', "")
        dob_str = request.POST.get('dob', "")
        try:
            dob = datetime.strptime(dob_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            dob = None
        zip = request.POST.get('zip', "")
        
        new_appointment = Appointment(
            first_name=first_name,
            last_name=last_name,
            phone_number=contact,
            password=password,  # Hash password before storing (security best practice)
            city=location,
            state=state,
            gender=gender,
            date_of_birth=dob,
            zip_code=zip,
        )
        # Save the new appointment to the database
        new_appointment.save()
        # Handle successful signup (optional)
        # ... (redirect to a confirmation page or display a success message)
        output = "Signup successful!"
        context = {'data': output}
        return render(request, 'Signup.html', context)

    else:
        # Handle GET requests (optional)
        return render(request, 'Signup.html')