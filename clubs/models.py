from django.db import models

# Create your models here.

class ClubAccount(models.Model):
    club_name       = models.CharField(null=True, default='', max_length=1000)
    club_website    = models.URLField(null=True)
    ig_id           = models.CharField(null=True, max_length=1000)
    club_email      = models.EmailField(null=True)


