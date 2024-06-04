from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import customer, Appointment
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def index(request):
    return render(request, 'home/index.html')

def schedule_view(request):
    return render(request, 'home/schedule.html')

from .models import customer

def schedule_view(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        cno = request.POST.get('cno')
        service = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Create and save the new customer object
        new_customer = customer(name=name, email=email, cno=cno, service=service, date=date, time=time)
        new_customer.save()

        # Pass the data to the submit page, including the primary key
        context = {
            'pk': new_customer.pk,  # Add the primary key to the context
            'name': name,
            'email': email,
            'cno': cno,
            'service': service,
            'date': date,
            'time': time,
        }
        return render(request, 'home/submit.html', context)

    return render(request, 'home/schedule.html')

def submit_view(request):
    if request.method == 'POST':
        # Handle the final submission logic here (e.g., save to database, send email, etc.)
        # For now, we'll just render a success page
        
        return render(request, 'home/success.html')
    
    return render(request, 'home/submit.html')

def success_view(request):
    return render(request, 'home/success.html')



def update_schedule_view(request, pk):
    n_customer = get_object_or_404(customer, pk=pk)

    if request.method == 'POST':
        # Extract form data
        n_customer.name = request.POST.get('name')
        n_customer.email = request.POST.get('email')
        n_customer.cno = request.POST.get('cno')
        n_customer.service = request.POST.get('service')
        n_customer.date = request.POST.get('date')
        n_customer.time = request.POST.get('time')

        # Save the updated customer object
        n_customer.save()

        # Redirect to a success page or display a success message
        return redirect('home/submit_update', pk=n_customer.pk)

    context = {
        'customer': n_customer
    }
    return render(request, 'home/update_schedule.html', context)

def submit_update_view(request, pk):
    n_customer = get_object_or_404(customer, pk=pk)
    return render(request, 'home/submit_update.html', {'customer': n_customer})


from datetime import datetime

def user_schedule(request):
    if request.method == 'POST':
        # Retrieve appointment details from the request
        service = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        # Convert date and time strings to datetime objects
        datetime_object = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
        
        # Create and save the appointment
        appointment = customer.objects.create(
            customer=request.user.customer ,  # Assuming one-to-one relationship between users and customers
            service=service,
            date=datetime_object.date(),
            time=datetime_object.time()
        )
        
        # Redirect to the user_schedule page
        return redirect('user_schedule')
    
    appointments = Appointment.objects.filter(customer__email=request.user.email)
    return render(request, 'home/user_schedule.html', {'appointments': appointments})


def edit_customer(request, pk):
    customer_instance = get_object_or_404(customer, pk=pk)
    # Assuming you have a Customer model and the instance retrieved here

    # Render the template with the customer instance in the context
    return render(request, 'home/update_schedule.html', {'customer': customer_instance})


def delete_customer(request, pk):
    customer_instance = get_object_or_404(customer, pk=pk)
    # Implement delete functionality
    customer_instance.delete()
    return redirect('list')







def services_view(request):
    # Define a list of services
    services = [
        {'name': 'Haircut', 'description': 'Professional haircut services for all ages.'},
        {'name': 'Massage', 'description': 'Relaxing massage therapy sessions.'},
        {'name': 'Car Maintenance', 'description': 'Comprehensive car maintenance services.'},
        # Add more services as needed
    ]
    return render(request, 'home/services.html', {'services': services})

def services_view(request):
    return render(request, 'home/services.html')




def list(request):
    customers = customer.objects.all().order_by('date','time')
    return render(request, 'home/list.html', {'customers': customers})



from .models import feedback

def contact_view(request):
    if request.method == 'POST':
        # Get the form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the feedback to the database
        Feedback = feedback(name=name, email=email, message=message)
        Feedback.save()

        # Redirect to a success page or return a success message
        return HttpResponse('Thank you for your feedback!')

    return render(request, 'home/contact.html')

















