from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponseRedirect

from django.contrib import messages

from django.conf import settings
 
from app_data.models import Actualite, Image

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from datetime import datetime

from app_data.forms import *
from app_data.models import NewsLetter, Actualite, MessageDuDirecteur

date_now = datetime.now()
date_now = date_now.strftime("%d, %b %Y à %Hh:%M:%S")

def send_newsLetter_fonction():
	actualites = Actualite.objects.all()
	emails = NewsLetter.objects.all()
	liste = []

	for email in emails:
		liste.append(email.email)


	for actualite in actualites:
		if actualite.newsLetter == False:

			content = {
				'titre' : actualite.titre,
				'image' : actualite.image.url,
				'date' : actualite.date,
				'description' : actualite.description,
				'id' : actualite.id
			}


			html_content = render_to_string("send_actualite.html", content)
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
				#objet
				'CEFA MB-FC : «{}»'.format(actualite.titre),

				#content
				text_content,

				#from email
				settings.EMAIL_HOST_USER,

				#rec
				liste
			)
			email.attach_alternative(html_content, "text/html")
			email.send()

			actualite.newsLetter = True
			actualite.save()

def accueil_view(request):

	actualites = Actualite.objects.all().order_by('-id')[:4]
	images = Image.objects.all().order_by('-id')[:8]
	linkVideo = VideoLink.objects.all().order_by('-id')[:1]

	print(linkVideo)

	template = "index.html"
	context = {
		'actualites': actualites,
		'images': images,
		'linkVideo': linkVideo
	}

	send_newsLetter_fonction()

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

		form_ins = InscriptionForm(request.POST)

		nom = poste.get('nom')
		prenom = poste.get('prenom')
		date_nais = poste.get('dateNais')
		genre = poste.get('genre')
		telephone = poste.get('telephone')
		ville = poste.get('ville')
		choix_cefa = poste.get('choix_cefa')
		email = poste.get('email')

		if len(nom) != 0:
			content = {
				'nom' : nom,
				'prenom' : prenom,
				'date_nais' : date_nais,
				'genre' : genre,
				'telephone' : telephone,
				'ville' : ville,
				'choix_cefa' : choix_cefa,
				'email' : email,
			}

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

			if form_ins.is_valid():
				form_ins.save()

			messages.success(request, "Demande d'inscription envoyée avec succès, Veuillez vous rendre à la direction avec les dossiers ci-dessus pour confirmer votre inscription !")
			return HttpResponseRedirect('/inscription/#message')
		else:
			messages.error(request, "Echec de l'envoie de la demande d'inscription, Ressayez en remplissant tous les champs ! !")
			return HttpResponseRedirect('/inscription/#message')

	form_ins = InscriptionForm()

	context = {
		'form': form_ins
	}

	return render(request, template, context)


def contact_view(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save()

			content = {
				'nom' : form.instance.nom,
				'telephone' : form.instance.telephone,
				'email' : form.instance.email,
				'objet' : form.instance.objet,
				'message' : form.instance.message
			}


			html_content = render_to_string("send_contact.html", content)
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
				#objet
				'CEFA MB-FC - Contact : «{}»'.format(form.instance.objet),

				#content
				text_content,

				#from email
				settings.EMAIL_HOST_USER,

				#rec
				['exaucengango20@gmail.com']
			)
			email.attach_alternative(html_content, "text/html")
			email.send()

			messages.success(request, "Message envoyé avec succès !")
			return redirect('contact_url')
		else:
			messages.error(request, "Message non envoyé, veuillez ressayé !")
			return redirect('contact_url')

	template = "contact.html"
	context = {}

	return render(request, template, context)



def about_view(request):

	message_dg = MessageDuDirecteur.objects.all().last()
	template = "about.html"
	context = {
		'message_dg' : message_dg,
	}

	return render(request, template, context)


def detail_message_view(request, id):

	message_dg = MessageDuDirecteur.objects.get(pk=id)
	template = "detail_message.html"
	context = {
		'message_dg' : message_dg,
	}

	return render(request, template, context)


def addNewsLetter(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		form_news = NewsLetterForm(request.POST)

		print(form_news.instance)
		print(NewsLetter.objects.filter(email=email).exists())

		if NewsLetter.objects.filter(email=email).exists() == False:
			
			if form_news.is_valid():
				form_news.save()
				messages.success(request, "Adresse enregistrée avec succès !")
				return HttpResponseRedirect('/#newsletter')

		else:
			messages.error(request, "L'addresse email existe déjà dans la base de donnée !")
			return HttpResponseRedirect('/#newsletter')
	form = NewsLetterForm()
	return HttpResponseRedirect('/#newsletter')
