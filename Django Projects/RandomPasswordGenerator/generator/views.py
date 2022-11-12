from django.shortcuts import render
from django.http import HttpResponse

import random
import string

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def password(request):

    length = int(request.GET.get('length'))

    lowerChar = string.ascii_lowercase #a-z
    upperChar = string.ascii_uppercase #A-Z
    digits = string.digits #0-9
    specialChar = string.punctuation


    characters = []

    if request.GET.get('upperCase'):
        characters.extend(list(upperChar))

    if request.GET.get('lowerCase'):
        characters.extend(list(lowerChar))

    if request.GET.get('Numbers'):
        characters.extend(list(digits))

    if request.GET.get('spChar'):
        characters.extend(list(specialChar))

    finalPassword = ""

    for x in range(length):
        finalPassword += random.choice(characters)


    context = {
        'length' : length,
        'finalPassword' : finalPassword,
    }


    return render(request, 'password.html', context)