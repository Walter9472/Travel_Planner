from django.db import models

# Create your models here.

#Modell Trip mit Feldern wie Titel, Startdatum, Enddatum, Beschreibung.
class Trip(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.TextField()

#Modell Destination (Name, Land, Kosten, Beschreibung).
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='destpics')
    country = models.CharField(max_length=100)
    # z.B. max. 6 Stellen insgesamt, 2 davon nach dem Komma: 9999.99
    price = models.DecimalField(max_digits=6,decimal_places=2)
    desc = models.TextField()

#Modell Activity (z.B. Museen, Restaurants) mit ForeignKey zu Trip oder Destination.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='actpics')
    desc = models.TextField()
    fk_id = models.ForeignKey()





