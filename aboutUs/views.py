from siteSettings.models import SiteSettings
from django.shortcuts import render
from .models import AboutUs



def aboutus_page(request):

    site_settings = SiteSettings.objects.last()
    aboutus = AboutUs.objects.last()
    title = site_settings.site_name + " - " + "درباره ما"
    context = {
        'aboutus': aboutus,
        'title': title,
        
    }
    
    return render(request,'AboutUs/aboutus_page/aboutus_page.html',context)