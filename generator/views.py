from django.shortcuts import render
import random
from string import *
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list()
    genpassword = ''

    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))
    if request.GET.get('numbers'):
        characters.extend(list(digits))
    if request.GET.get('spcharacters'):
        characters.extend(list(punctuation))
    else:
        characters.extend(list(printable))

    length = int(request.GET.get('length', 8))

    for x in range(length):
        genpassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': genpassword})