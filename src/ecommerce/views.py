from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth import authenticate, get_user_model

def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "About/about_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Página de contato",
        "content": "Bem-vindo a página de contato",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    #if request.method == "POST":
        #print(request.POST)
        #print(request.POST.get('Nome_Completo'))
        #print(request.POST.get('email'))
        #print(request.POST.get('Mensagem'))
    return render(request, "Contact/contact_page.html", context)