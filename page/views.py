from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, Materias, MateriaAluno
from .forms import UserForm, MateriaAlunoForm, MateriaAlunoDeleteAllForm

import numpy as np

def homepage(request):

    context = {}

    return render(request, 'homepage.html', context=context)

@login_required
def perfil(request):

    if(request.POST):
        if("excluir_materia_aluno" in request.POST.dict().keys()):
            id_materia_aluno_a_excluir = request.POST.dict()['excluir_materia_aluno']
            materia_aluno_a_excluir = MateriaAluno.objects.filter(id=id_materia_aluno_a_excluir)
            materia_aluno_a_excluir.delete()
    
    selected_user_id = ""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            selected_user_id = form.cleaned_data['user'].id
            
    else:
        form = UserForm()

    aluno_logado = request.user

    if(selected_user_id != ""):
        aluno_selecionado = User.objects.filter(id=selected_user_id).first()
        materias_aluno = MateriaAluno.objects.filter(aluno=aluno_selecionado)
    else:
        materias_aluno = MateriaAluno.objects.filter(aluno=aluno_logado)

    context = {'materias_aluno_logado':materias_aluno,
               'dias_semana': np.arange(2,9),
               'alunos': User.objects.all(),
               'form': form,
               }

    return render(request, 'perfil.html', context=context)

@user_passes_test(lambda u: u.is_superuser)
def add_materia_aluno(request):
    if request.method == 'POST':
        form = MateriaAlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_materia_aluno')
    else:
        form = MateriaAlunoForm()
    return render(request, 'add_materia_form.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_all_materias_aluno(request):
    if request.method == 'POST':
        form = MateriaAlunoDeleteAllForm(request.POST)
        if form.is_valid():
            usuario_aluno = form.cleaned_data["user"]
            materias_aluno_deletar = MateriaAluno.objects.filter(aluno=usuario_aluno)

            for materia in materias_aluno_deletar:
                materia.delete()

            return redirect('perfil')
    else:
        form = MateriaAlunoDeleteAllForm()
    return render(request, 'delete_all_materia_form.html', {'form': form})