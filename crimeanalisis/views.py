from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'crimeanalisis/inicio.html')
  
def upload(request):
    if request.method == 'POST':
        # Aquí iría la lógica para procesar la imagen cargada
        # y redireccionar a la página de resultados
        return HttpResponse("Imagen recibida. Procesando...")
    return render(request, 'crimeanalisis/upload.html')

def resultados(request):
    # Simula la obtención de resultados del análisis
    objects = [{'name': 'Objeto1', 'x': 50, 'y': 100}]
    return render(request, 'crimeanalisis/resultados.html', {'objects': objects})

def historial(request):
    return render(request, 'crimeanalisis/historial.html')
