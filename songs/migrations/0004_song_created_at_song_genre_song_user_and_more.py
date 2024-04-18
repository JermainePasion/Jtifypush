# Generated by Django 5.0.1 on 2024-02-14 17:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_remove_song_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('Hip-Hop', 'Hip-Hop'), ('R&B', 'R&B'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('Country', 'Country'), ('Jazz', 'Jazz'), ('Classical', 'Classical'), ('Blues', 'Blues'), ('Electronic', 'Electronic'), ('Reggae', 'Reggae'), ('Folk', 'Folk'), ('Punk', 'Punk'), ('Metal', 'Metal'), ('Soul', 'Soul'), ('Funk', 'Funk'), ('Disco', 'Disco'), ('Gospel', 'Gospel'), ('House', 'House'), ('Techno', 'Techno'), ('Dubstep', 'Dubstep'), ('Trap', 'Trap'), ('Drum & Bass', 'Drum & Bass'), ('Grime', 'Grime'), ('Garage', 'Garage'), ('Salsa', 'Salsa'), ('Afrobeat', 'Afrobeat'), ('Highlife', 'Highlife')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]
