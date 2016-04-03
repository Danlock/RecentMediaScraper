from django.db import models

# Create your models here.
# class Media_Base(models.Model):
#     class Meta:
#         abstract = True




class Movie(models.Model):
    title = models.CharField(max_length=300,default="")
    release_date = models.DateTimeField('date released',default="")
    popularity = models.DecimalField(max_digits=9, decimal_places=8,default=0.0)
    backdrop_path = models.CharField(max_length=50,default="")
    genre_ids = models.CommaSeparatedIntegerField(max_length=30,default=[])
    poster_path = models.CharField(max_length=50,default="")
    vote_average = models.DecimalField(max_digits=3, decimal_places=1,default=0.0)
    media_id = models.PositiveIntegerField('id',default=1)
    adult = models.BooleanField('adult',default=False)
    vote_count = models.PositiveIntegerField('vote_count',default="0")
    original_language = models.CharField(max_length=3,default="")
    overview = models.TextField('overview',default="")

    def __str__(self):
        return self.title

# class TVShow(Media_Base):
#     lead_actors = models.CharField(max_length=300)

# class Anime(Media_Base):
#     animation_studio = models.CharField(max_length=50)
#     original_title = models.CharField(max_length=300)
