from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


@require_http_methods(['GET'])
def index(request):
    name = request.session['name']
    password = request.session['password']
    return HttpResponse("{0},{1} login success".format(name,password))


def login(request):
    if request.method == 'GET':
        return render(request, template_name='login.html')
    else:
        name = request.POST['name']
        password = request.POST['password']
        if name == "fei" and password == "123":
            response = HttpResponse("hello {0}".format(name))
            request.session['name'] = name
            request.session['password'] = password
            return redirect("/index")
        else:
            return redirect(reverse(viewname='login'))

def page_not_found(request, exception):
    return render(request, '404.html')