from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cars_view(request):
    html = '''
    <html>
        <head>
            <title>Meus Carros</title>
        </head>
        <body>
            <h1>Carros do Fill</h1>
            <h3>Só Carro TOP!</h3>
        </body>
    </html>
    '''
    return HttpResponse(html)