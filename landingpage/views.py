# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


def home(request):
    enviado = False  # ← Definimos por defecto

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extraer datos
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']

            contenido = f"""
            Nombre: {nombre}
            Correo: {correo}
            Teléfono: {telefono}
            Mensaje: {mensaje}
            """

            send_mail(
                subject=f"Consulta desde Servelec Ingeniería - {nombre}",
                message=contenido,
                from_email='contacto@servelec-ingenieria.cl',
                recipient_list=['contacto@servelec-ingenieria.cl'],
               fail_silently=False,
            )

        
            enviado = True  # ← Marcamos que se envió correctamente
            form = ContactForm()  # ← Opcional: limpiar el formulario
    else:
        form = ContactForm()

    return render(request, 'landingpage/home.html', {
        'form': form,
        'enviado': enviado
    })



def contacto(request):
    return render(request, 'landingpage/contact.html')

def nosotros(request):
    return render(request, 'landingpage/nosotros.html')

def servicios(request):
    return render(request, 'landingpage/servicios.html')

def contact_exitoso(request):
    return render(request, 'landingpage/contact_exitoso.html')









