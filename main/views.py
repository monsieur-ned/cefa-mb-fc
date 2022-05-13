from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponseRedirect

from django.contrib import messages

from django.conf import settings
 
from app_data.models import Actualite, Image

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from datetime import datetime

date_now = datetime.now()
date_now = date_now.strftime("%d, %b %Y à %Hh:%M:%S")

def accueil_view(request):

	actualites = Actualite.objects.all().order_by('-id')[:4]
	images = Image.objects.all().order_by('-id')[:8]

	template = "index.html"
	context = {
		'actualites': actualites,
		'images': images,
	}

	return render(request, template, context)


def actualites_view(request):

	actualites = Actualite.objects.all().order_by('-id') 

	template = "actualites.html"
	context = {
		'actualites': actualites,
	}

	return render(request, template, context)


def actualite_detail_view(request, id):

	actualite = get_object_or_404(Actualite, id=id)

	template = "actualite_detail.html"
	context = {
		'actualite': actualite
	}

	return render(request, template, context)


def inscription_view(request):
	template = "inscription.html"

	if request.method == "POST":
		poste = request.POST

		nom = poste.get('nom')
		prenom = poste.get('prenom')
		date_nais = poste.get('dateNais')
		genre = poste.get('genre')
		telephone = poste.get('tel')
		ville = poste.get('ville')
		choix_cefa = poste.get('cefa')

		if len(nom) != 0:
			content = {
				'nom' : nom,
				'prenom' : prenom,
				'date_nais' : date_nais,
				'genre' : genre,
				'telephone' : telephone,
				'ville' : ville,
				'choix_cefa' : choix_cefa,
			}

			print(content)

			html_content = render_to_string("send_mail.html", content)
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
				#objet
				'Depuis le site officiel de CEFA : «Inscription» ({})'.format(date_now),

				#content
				text_content,

				#from email
				settings.EMAIL_HOST_USER,

				#rec
				['exaucengango20@gmail.com']
			)
			email.attach_alternative(html_content, "text/html")
			email.send()

			messages.success(request, "Demande d'inscription envoyée avec succès, nous vous contacterons sous peu !")
			return HttpResponseRedirect('/inscription/#message')
		else:
			messages.error(request, "Echec de l'envoie de la demande d'inscription, Ressayez en remplissant tous les champs ! !")
			return HttpResponseRedirect('/inscription/#message')

	context = {}

	return render(request, template, context)


def contact_view(request):
	template = "contact.html"
	context = {}

	return render(request, template, context)