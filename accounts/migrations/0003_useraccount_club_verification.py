# Generated by Django 3.0.8 on 2020-07-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200718_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='club_verification',
            field=models.BooleanField(default=False),
        ),
    ]
