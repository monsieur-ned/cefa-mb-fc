from django.db import models
from ckeditor.fields import RichTextField

class Inscription(models.Model):
	nom = models.CharField(max_length=100)
	prenom = models.CharField(max_length=100)
	date_naissance = models.DateField()
	genre = models.CharField(max_length=5)
	telephone = models.CharField(max_length=50)
	ville = models.CharField(max_length=100) 
	choix_cefa = models.CharField(max_length=100)

	date = models.DateTimeField(auto_now_add=True)

class Actualite(models.Model):
	image = models.FileField(upload_to='images-actualites/')
	titre = models.CharField(max_length=100)
	description = RichTextField()

	date = models.DateField(auto_now_add=True)

class Image(models.Model):
	image = models.FileField(upload_to='images-galerie/')
	description = models.CharField(max_length=255)
	
	date = models.DateField(auto_now_add=True)