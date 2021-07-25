from django.db import models

class Home(models.Model):
    links = models.CharField(max_length=255)
    texto_da_home = models.TextField()
