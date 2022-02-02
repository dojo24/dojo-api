from django.db import models

class Characters(models.Model):
    name = models.CharField(max_length=255)
    birthDay = models.CharField(max_length=255, blank=True)
    spouse = models.CharField(max_length=255, blank=True)
    voice = models.CharField(max_length=255, blank=True)
    img = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.name


class Squishies(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.name