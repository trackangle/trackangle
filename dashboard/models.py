from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.core.exceptions import ValidationError

#todo photos as input
#todo Hotel Name or other acctype related fields as input

class AccomodationType(models.Model):
    # Variable: title
    title = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    # Variable: title
    title = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.title

class Route(models.Model):

    # Variable: title
    title = models.CharField(max_length=50, unique=True, null=False, blank=False)

    #Variable: rate
    rate = models.IntegerField(null=False, blank=False)

    #Variable: expense
    expense = models.CharField(max_length=20)

    #Variable: Tag
    tag = models.ManyToManyField(Tag)

    #todo: need to decide max length of explanation
    #Variable: explanation
    explanation = models.CharField(max_length=500)


    def __str__(self):
        return self.title

class VisitedPlaces(models.Model):

    #Variable: Route
    route = models.ForeignKey(Route)

    #Variable: title
    title = models.CharField(max_length = 50, null = False, blank=False)

    #Variable: accomodationtype
    acc_type = models.ManyToManyField(AccomodationType)

    #todo: need to decide max length of explanation
    #Variable: explanation
    explanation = models.CharField(max_length=500)

    #Variable: expense
    expense = models.CharField(max_length=20)

    def __str__(self):
        return self.route.title+":"+self.title


class ArchitectureAndBuildings(models.Model):

    #Variable: Visited Places
    visited_places = models.ForeignKey(VisitedPlaces)

    #Variable: title
    title = models.CharField(max_length = 50, null = False, blank=False)

    def __str__(self):
        return self.title

class Outdoor(models.Model):

    #Variable: Visited Places
    visited_places = models.ForeignKey(VisitedPlaces)

    #Variable: title
    title = models.CharField(max_length = 50, null = False, blank=False)

    def __str__(self):
        return self.title

class Food(models.Model):

    #Variable: Visited Places
    visited_places = models.ForeignKey(VisitedPlaces)

    #Variable: title
    title = models.CharField(max_length = 50, null = False, blank=False)

    def __str__(self):
        return self.title

class EntertainmentAndArt(models.Model):

    #Variable: Visited Places
    visited_places = models.ForeignKey(VisitedPlaces)

    #Variable: title
    title = models.CharField(max_length = 50, null = False, blank=False)

    def __str__(self):
        return self.title

class ShopAndServices(models.Model):

    #Variable: Visited Places
    visited_places = models.ForeignKey(VisitedPlaces)

    #Variable: title
    title = models.CharField(max_length = 50, null = False, blank=False)

    def __str__(self):
        return self.title















