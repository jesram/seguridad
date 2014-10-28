from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente

def get_all(request, template_name='all_pacientes.html'):
    pacientes = Paciente.objects.all()
    data = {}
    data['pacientes'] = pacientes
    return render(request, template_name, data)

def crear_paciente(request, template_name='paciente_form.html'):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('paciente_list')
    return render(request, template_name, {'form': form})

def update_paciente(request, pk, template_name='paciente_form.html'):
    paciente = get_object_or_404(Paciente, pk=pk)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('paciente_list')
    return render(request, template_name, {'form': form})


def delete_paciente(request, pk, template_name='confirm_delete_px.html'):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.POST:
        paciente.delete()
        return redirect('paciente_list')
    return render(request,template_name, {'object': paciente})

