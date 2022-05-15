from app_data.models import *
from django.forms import *

class NewsLetterForm(ModelForm):
	class Meta:
		model = NewsLetter
		fields = ['email']


class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

class InscriptionForm(ModelForm):
	class Meta:
		model = Inscription
		fields = [
		'nom',
		'prenom',
		'date_naissance', 
		'genre',
		'telephone',
		'email',
		'ville',
		'choix_cefa'
		]

		widgets = {
			'nom' : TextInput(attrs={'class':'form-control', 'required':'', 'placeholder' : 'Votre nom de famille'}),
			'prenom' : TextInput(attrs={'class':'form-control', 'required':'', 'placeholder' : 'Votre prénom'}),
			'date_naissance' : DateInput(attrs={'class':'form-control', 'required':'', 'placeholder' : 'Votre nom ou pseudo'}),
			'genre' : TextInput(attrs={'class':'form-control', 'required':''}),
			'telephone' : TextInput(attrs={'class':'form-control', 'required':'', 'placeholder' : 'Numéro de téléphone valide'}),
			'email' : EmailInput(attrs={'class':'form-control', 'required':'', 'placeholder' : 'Adresse electronique'}),
			'ville' : TextInput(attrs={'class':'form-control', 'required':'', 'placeholder' : 'Votre ville de residence'}),
			'choix_cefa' : TextInput(attrs={'class':'form-control', 'required':''}),
		}