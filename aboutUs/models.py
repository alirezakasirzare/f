from django.db import models

class AboutUs(models.Model):
    description = models.TextField()
    team_image = models.ImageField(upload_to='static_cdn/media_root/TeamImage',)
