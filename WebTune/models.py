from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(upload_to='=logos/', blank=True)

    def __str__(self):
        return self.album_title + ' => ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='mp3/', blank=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
