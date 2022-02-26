from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect



def index(request):

    return render(request, 'index.html')

def logout(request):
    django_logout(request)
    domain = 'dev-pp15pg6x.auth0.com'
    client_id = 'zJVkU28u1rE63gmIEbYmZz3pLzd5Z0Yw'
    return_to = 'http://localhost:8082'
    return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')