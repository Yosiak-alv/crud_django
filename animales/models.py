from django.db import models

# Create your models here.
class Animal(models.Model):
    #id = models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False,null=False)
    especie = models.CharField(max_length=100,blank=False,null=False)    

    def __str__(self):
        return self.name + ' ; ' + self.especie