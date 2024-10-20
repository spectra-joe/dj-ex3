from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, "Registration successful!")
            return redirect('success')  # Redirect to the success page
        else:
            messages.error(request, "There was an error with your form.")
    else:
        form = RegistrationForm()

    return render(request, 'registerapp/register.html', {'form': form})

def success_view(request):
    return render(request, 'registerapp/success.html')
