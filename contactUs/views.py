from siteSettings.models import  SiteSettings
from django.contrib import messages
from django.shortcuts import render
from .forms import contactusForm
from .models import ContactUs


"""
Views:

    contactus_page() # Request a call

"""

def contactus_page(request):
    site_settings = SiteSettings.objects.last()
    title = site_settings.site_name + " - " + "تماس با ما"
    form = contactusForm(request.POST)
    if form.is_valid():
        firstName = form.cleaned_data['firstName']
        lastName = form.cleaned_data['lastName']
        email = form.cleaned_data['email']
        contact_number = form.cleaned_data['contact_number']
        company_name = form.cleaned_data['company_name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        ContactUs.objects.create(firstName=firstName,lastName=lastName,email=email,contact_number=contact_number,company_name=company_name,subject=subject,message=message)
        messages.success(request, 'Your profile was updated.')
        
    context = {
        'title': title,
        'contactusForm': contactusForm,
    }
    return render(request,'ContactUs/contactus_page/contactus_page.html',context)
