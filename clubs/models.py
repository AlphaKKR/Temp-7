from django.db import models

# Create your models here.

class ClubAccount(models.Model):
    club_name       = models.CharField(null=True, default='', max_length=1000)
    club_website    = models.URLField(null=True)
    ig_id           = models.CharField(null=True, max_length=1000)
    club_email      = models.EmailField(null=True, unique=True)
    club_logo       = models.ImageField(upload_to='clubs/logos', default='', null=True)


    def __str__(self):
        return self.club_name

class ClubEvent(models.Model):
    club_email      = models.ForeignKey(ClubAccount, on_delete=models.CASCADE, null=True)
    event_name      = models.CharField(max_length=100 ,default='', null=True)
    event_desc      = models.TextField(default='', max_length=1000, null=True)
    event_poster    = models.ImageField(upload_to='clubs/events', default='', null=True)
    event_url       = models.URLField(default='', null=True)

    def __str__(self):
        return self.club_email

class ClubBigEvent(models.Model):
    club_name       = models.ForeignKey(ClubAccount, on_delete=models.CASCADE, null=True)
    event_desc      = models.TextField(default='', max_length=1000, null=True)
    image           = models.ImageField(upload_to='clubs/events', default='', null=True)
    event_url       = models.URLField(default='', null=True)

    def __str__(self):
        return self.club_name

class Recruitment(models.Model):
    club_email      = models.ForeignKey(ClubAccount, on_delete=models.CASCADE, null=True)
    rec_date_time   = models.DateTimeField(null=True)
    rec_desc        = models.TextField(max_length=1000, default='', null=True)

    def __str__(self):
        return self.club_email


class BigRecruitment(models.Model):
    club_name       = models.ForeignKey(ClubAccount, on_delete=models.CASCADE, null=True)
    rec_date_time   = models.DateTimeField(null=True)
    rec_desc        = models.TextField(max_length=1000, default='', null=True)
