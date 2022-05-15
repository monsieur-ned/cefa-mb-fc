from django.db import models
from ckeditor.fields import RichTextField

class Inscription(models.Model):
	nom = models.CharField(max_length=100)
	prenom = models.CharField(max_length=100)
	date_naissance = models.DateField()
	genre = models.CharField(max_length=20)
	telephone = models.CharField(max_length=50)
	email = models.EmailField(null=True, blank=True)
	ville = models.CharField(max_length=100) 
	choix_cefa = models.CharField(max_length=250)

	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.nom} {self.prenom} - {self.choix_cefa}'

class Actualite(models.Model):
	image = models.FileField(upload_to='images-actualites/')
	titre = models.CharField(max_length=100)
	description = RichTextField()
	newsLetter = models.BooleanField(default=False)

	date = models.DateField(auto_now_add=True)

class Image(models.Model):
	image = models.FileField(upload_to='images-galerie/')
	description = models.CharField(max_length=255)
	
	date = models.DateField(auto_now_add=True)

class NewsLetter(models.Model):
	email = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email

class MessageDuDirecteur(models.Model):
	photo = models.FileField("Profil du directeur", upload_to='profile-directeur/')
	nom = models.CharField("Nom complet du directeur", max_length = 100)
	message = RichTextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nom

class Contact(models.Model):
	nom = models.CharField(max_length=100)
	telephone = models.CharField(max_length=35)
	email = models.EmailField(null=True, blank=True)
	objet = models.CharField(max_length=255)
	message = RichTextField()

	def __str__(self):
		return f'{self.nom}'