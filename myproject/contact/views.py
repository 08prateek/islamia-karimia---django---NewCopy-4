
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()  # Save form data to database


            request.session['success_message'] = "Your form has been submitted successfully."
            return redirect('contact')
    else:
        form = ContactForm()

    success_message = request.session.pop('success_message', None)
    return render(request, 'contact/contact.html', {'form': form, 'success_message': success_message})