from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print username, password
        user = authenticate(request, username=username, password=password)
    else:
        return render(request, template_name="login.html")
    if user is not None:
        print "login"
        login(request, user)
        return render(request, template_name='home.html')
    else:
        print "json"
        return JsonResponse({'message': "Error al loguear, verifique su usuario y password!"},
                            status=400)


def home(request):
    return render(request, template_name='home.html')
