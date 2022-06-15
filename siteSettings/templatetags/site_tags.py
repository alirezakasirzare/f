from django import template
from siteSettings.models import SiteSettings

register = template.Library()

@register.simple_tag
def site_settings():
    return SiteSettings.objects.first()