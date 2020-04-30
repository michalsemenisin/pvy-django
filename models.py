from django.db import models
from django.urls import reverse

# Create your models here.
def img_path(instance, filename):
    return "planeta/" + str(instance.id) + "/img/" + filename

class Star(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Star name")
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Discovery(models.Model):
    method = models.CharField(choices=(('imaging','Imaging'),
                                      ('radial_velocity','Radial Velocity'),
                                      ('transit','Transit'),
                                      ('eclipse_timing_variations','Eclipse Timing Variations')), blank=True, max_length = 35)
    
    
    class Meta:
        ordering = ["method"]

    def __str__(self):
        return self.method

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    last_name = models.CharField(max_length=50, verbose_name="Last surname")
    role = models.CharField(choices=(('redaktor','Redaktor'),
                                    ('redaktor_ve_vycviku','Redaktor ve vycviku'),
                                    ('sefredaktor','Šéfredaktor')), blank=True, max_length=25)
    class Meta:
        ordering = ["role", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Exoplanet(models.Model):
    planet_name = models.CharField(max_length=30, verbose_name="Planet name")
    image = models.ImageField(upload_to=img_path, blank=True, null=True, verbose_name="Image")
    discovery_date = models.DateField(blank=True, null=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.", verbose_name="Discovery date")
    discovery = models.ForeignKey(Discovery, on_delete=models.CASCADE)
    radius = models.IntegerField(blank=True, null=True, verbose_name="Radius")
    distance = models.IntegerField(blank=True, null=True, verbose_name="Distance")
    mass = models.IntegerField(blank=True, null=True, verbose_name="Mass")

    class Meta:
        ordering = ["planet_name", "discovery"]

    def __str__(self):
        return f"{self.planet_name}"
    



