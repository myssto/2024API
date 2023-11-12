# Generated by Django 4.2.6 on 2023-11-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_tournamentplayer_is_organizer'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tournamentplayer',
            index=models.Index(fields=['osu_user_id'], name='userauth_to_osu_use_e7420a_idx'),
        ),
    ]
