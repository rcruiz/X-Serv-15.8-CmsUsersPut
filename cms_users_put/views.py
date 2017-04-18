from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Page
from django.contrib.auth import logout, login


def userLog(request):
    if request.user.is_authenticated():
        respuesta = "Logged in as " + request.user.username + ". "
        respuesta += '<a href="/logout">Logout</a><br/><br/>'
    else:
        respuesta = "Not logged in. " + '<a href="/login">Login</a><br/>'
    return respuesta

def mostrar_todo(request):
    respuesta = userLog(request)
    lPages = Page.objects.all()
    respuesta += "<ul> Los contenidos almacenados son:<br/>"
    for page in lPages:
        respuesta += '<li><a href="' + str(page.id) + '">'
        respuesta += page.name + '</a></li>'
    respuesta += "</ul>"
    return HttpResponse(respuesta)

def mostrar_id(request, page_id):
    respuesta = userLog(request)
    try:
        contenido = Page.objects.get(id=int(page_id))
        respuesta += contenido.name + ' : ' + contenido.page
    except Page.DoesNotExist:
        respuesta += 'Pagina no encontrada'
    return HttpResponse(respuesta)

@csrf_exempt
def contenido(request, recurso):
    cuerpo = request.body
    formulario = "<form method = POST action=''" + recurso + ">"
    formulario += "Nombre: <input type='text' name='name'><br/>"
    formulario += "Página: <input type='text' name='page'><br/>"
    formulario += "<input type='submit' value='Enviar'></form>"
    respuesta = userLog(request)
    if request.method == 'GET':
        try:
            contenido = Page.objects.get(name=recurso)
            respuesta += '<a href="/' + contenido.name + '">/'
            respuesta += contenido.name + '</a>' + ' : ' + contenido.page
        except Page.DoesNotExist:
            respuesta += "Página no almacenada. Insértela" + formulario
    elif request.method == 'PUT':
        if request.user.is_authenticated():
            try:  # Actualiza el contenido de la pagina
                contenidoAlmac = Page.objects.get(name=recurso)
                contenidoAlmac.page = cuerpo
                contenidoAlmac.save()
            except Page.DoesNotExist:
                contenido = Page(name=recurso, page=cuerpo)
                contenido.save()
            respuesta += "La página ha sido actualizada"
        else:
            respuesta += "Usted no está registrado. No puede modificar contenido"
    elif request.method == 'POST':
        if request.user.is_authenticated():
            nombre = request.POST['name']
            pag = request.POST['page']
            contenido = Page(name=nombre, page=pag)
            contenido.save()
            respuesta += "Página guardada"
        else:
            respuesta += "Usted no está registrado. No puede modificar contenido"
    else:
        respuesta += "Metodo introducido no válido"
    return HttpResponse(respuesta)
