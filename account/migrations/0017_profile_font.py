# Generated by Django 5.0.1 on 2024-02-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_rename_song_likedsong_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='font',
            field=models.CharField(choices=[('Default', 'Default'), ('Open Sans', 'Open Sans'), ('Young Serif', 'Young Serif'), ('Roboto Slab', 'Roboto Slab'), ('Roboto Mono', 'Roboto Mono'), ('Noto Sans JP', 'Noto Sans JP'), ('Yuji Hentaigana Akari', 'Yuji Hentaigana Akari'), ('Agbalumo', 'Agbalumo'), ('Alegreya Sans', 'Alegreya Sans'), ('Montserrat', 'Montserrat'), ('Edu TAS Begginer', 'Edu TAS Begginer'), ('Playpen Sans', 'Playpen Sans')], default='Default', max_length=255),
        ),
    ]