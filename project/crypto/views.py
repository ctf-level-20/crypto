from django.shortcuts import render
from cryptography.fernet import Fernet
from django.http import HttpResponse
# Create your views here.
def home(request):

    return render(request,"ht.html")

def encrypt(request):
    try:
        sym_key = "I0oy3rjnIF6GELamz5EEmnkf-cEAnM2UqmQaZx8RkC0="
        message = request.POST['plain']
        f = Fernet(sym_key)
        data = bytes(message, 'utf-8')
        token = f.encrypt(data)
        context ={
            'a':token
        }
    except Exception:
        token = "Incorrect Value"
        context = {
            'b': token
        }
    resp = render(request,"ht.html",context)
    # set http response header and value.
    resp['x-fernet-secret'] = 'I0oy3rjnIF6GELamz5EEmnkf-cEAnM2UqmQaZx8RkC0='
    return resp

def decrypt(request):
    try:
        sym_key = "I0oy3rjnIF6GELamz5EEmnkf-cEAnM2UqmQaZx8RkC0="
        message = request.POST['cipher']
        f = Fernet(sym_key)
        data = bytes(message, 'utf-8')
        token = f.decrypt(data)
        context ={
            'b':token
        }
    except Exception:
        token = "Incorrect Value"
        context = {
            'b': token
        }
    resp = render(request,"ht.html",context)
    # set http response header and value.
    resp['x-fernet-secret'] = 'I0oy3rjnIF6GELamz5EEmnkf-cEAnM2UqmQaZx8RkC0='
    return resp