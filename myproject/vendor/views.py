from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VendorRegistrationForm, TenderForm
from .models import Tender,Vendor, TenderApplication
from django.contrib.auth import logout
from contact.models import Contact
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactNumberForm



def register_vendor(request):
    success = False
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = VendorRegistrationForm()  # Reset the form after successful submission
            request.session['success_message'] = "Your form has been submitted successfully."
            return redirect('register_vendor')  # Redirect to the same view to avoid resubmission on refresh
    else:
        form = VendorRegistrationForm()
        
    success_message = request.session.pop('success_message', None)    
    return render(request, 'vendor/register.html', {'form': form, 'success_message': success_message})

@login_required
def create_tender(request, tender_id=None):
    if not request.session.get('create_tender_logged_in'):
        logout(request)
        return redirect('login')

    if tender_id:
        tender = get_object_or_404(Tender, id=tender_id)
        if request.method == 'POST':
            if 'update' in request.POST:
                form = TenderForm(request.POST, request.FILES, instance=tender)
                if form.is_valid():
                    form.save()
                    return redirect('create_tender')
            elif 'delete' in request.POST:
                tender.delete()
                return redirect('create_tender')
        else:
            form = TenderForm(instance=tender)
    else:
        tender = None
        if request.method == 'POST':
            form = TenderForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('create_tender')
        else:
            form = TenderForm()

    tenders = Tender.objects.all()
    vendors = Vendor.objects.all()
    contacts = Contact.objects.all()
    tender_applications = TenderApplication.objects.all()

    return render(request, 'vendor/create_tender.html', {
        'form': form,
        'tender': tender,
        'tenders': tenders,
        'vendors': vendors,
        'contacts': contacts,
        'tender_applications': tender_applications
    })

def tender_list(request):
    tenders = Tender.objects.all()
    return render(request, 'tender_list.html', {'tenders': tenders})

def tender_list(request):
    tenders = Tender.objects.all()
    return render(request, 'vendor/tender_list.html', {'tenders': tenders})

@csrf_exempt
def apply_tender(request):
    if request.method == "POST":
        form = ContactNumberForm(request.POST)
        if form.is_valid():
            contact_number = form.cleaned_data['contact_number']
            tender_id = request.POST.get("tender_id")

            try:
                vendor = Vendor.objects.get(contact=contact_number)
            except Vendor.DoesNotExist:
                return JsonResponse({"message": "You need to register yourself first."}, status=400)

            if TenderApplication.objects.filter(vendor=vendor, tender_id=tender_id).exists():
                return JsonResponse({"message": "You have already applied for this tender."}, status=400)

            tender = Tender.objects.get(id=tender_id)
            TenderApplication.objects.create(
                tender=tender,
                vendor=vendor,
                vendor_name=vendor.name,
                vendor_contact=vendor.contact,
                vendor_email=vendor.email,
                tender_title=tender.title
            )
            return JsonResponse({"message": "You have successfully applied for this tender."})

        return HttpResponseBadRequest("Invalid contact number")

    return HttpResponseBadRequest("Invalid request method")