# Generated by Django 3.0.8 on 2020-07-19 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20200719_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubBigEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_desc', models.TextField(default='', max_length=1000, null=True)),
                ('image', models.ImageField(default='', null=True, upload_to='clubs/events')),
                ('event_url', models.URLField(default='', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ClubBigEvents',
        ),
        migrations.AddField(
            model_name='bigrecruitment',
            name='club_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.ClubAccount'),
        ),
        migrations.AlterField(
            model_name='clubaccount',
            name='club_email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='clubbigevent',
            name='club_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.ClubAccount'),
        ),
    ]
