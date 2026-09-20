from django.shortcuts import render, redirect
from .models import Empresa, Conductor, Licencia, Ruta

def dashboard(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo_form')
        
        if tipo == 'empresa':
            Empresa.objects.create(
                nombre=request.POST.get('nombre'),
                nit=request.POST.get('nit')
            )
        elif tipo == 'conductor':
            empresa_id = request.POST.get('empresa')
            empresa_obj = Empresa.objects.get(id=empresa_id)
            Conductor.objects.create(
                nombre=request.POST.get('nombre'),
                documento=request.POST.get('documento'),
                empresa=empresa_obj
            )
        elif tipo == 'licencia':
            conductor_id = request.POST.get('conductor')
            conductor_obj = Conductor.objects.get(id=conductor_id)
            Licencia.objects.create(
                numero=request.POST.get('numero'),
                categoria=request.POST.get('categoria'),
                conductor=conductor_obj
            )
        elif tipo == 'ruta':
            nueva_ruta = Ruta.objects.create(
                nombre=request.POST.get('nombre'),
                origen=request.POST.get('origen'),
                destino=request.POST.get('destino')
            )
            conductores_ids = request.POST.getlist('conductores')
            if conductores_ids:
                nueva_ruta.conductores.set(conductores_ids)

        return redirect('dashboard')

    contexto = {
        'empresas': Empresa.objects.all(),
        'conductores': Conductor.objects.select_related('empresa').all(),
        'licencias': Licencia.objects.select_related('conductor').all(),
        'rutas': Ruta.objects.prefetch_related('conductores').all(),
        'total_empresas': Empresa.objects.count(),
        'total_conductores': Conductor.objects.count(),
        'total_licencias': Licencia.objects.count(),
        'total_rutas': Ruta.objects.count(),
    }
    return render(request, 'app_code_rider/dashboard.html', contexto)