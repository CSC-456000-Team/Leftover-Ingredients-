import os
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .connect_api import get_recipe_ids, get_recipes
from django.contrib import messages

# from django.http import HttpResponse


def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html", {"title": "About"})


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        recipe_ids = get_recipe_ids(searched)
        recipes = get_recipes(recipe_ids)
        return render(
            request, "main/search.html", {"searched": searched, "recipes": recipes}
        )
    else:
        return render(request, "main/search.html", {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Us Message" 
            body = {
            'name': form.cleaned_data['contact_name'],  
            'email': form.cleaned_data['contact_email'], 
            'message':form.cleaned_data['contact_message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'tttesttting6@gmail.com', 'tttesttting6@gmail.com')
                #send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
                messages.info(request, 'Your feedback has been sent successfully!') 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            else:
                messages.info(request, 'Your feedback has been sent successfully!')
            return redirect ("main:index")
      
    form = ContactForm()
    return render(request, "main/index.html", {'form':form})