from django.db import models

# Create your models here.

class Playlist(models.Model):
    user = models.EmailField()
    name = models.CharField(max_length=60, default='')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.user


class Song(models.Model):
    song_id = models.CharField(max_length=60)# The spotify id.
    pos_votes = models.PositiveIntegerField(default=0)
    neg_votes = models.PositiveIntegerField(default=0)
    pos = models.PositiveIntegerField(default=1)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)