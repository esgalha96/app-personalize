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

    materias_aluno_domingo = materias_aluno.filter(dia_semana = 1)
    materias_aluno_segunda = materias_aluno.filter(dia_semana = 2)
    materias_aluno_terca = materias_aluno.filter(dia_semana = 3)
    materias_aluno_quarta = materias_aluno.filter(dia_semana = 4)
    materias_aluno_quinta = materias_aluno.filter(dia_semana = 5)
    materias_aluno_sexta = materias_aluno.filter(dia_semana = 6)
    materias_aluno_sabado = materias_aluno.filter(dia_semana = 7)

    context = {
                'materias_aluno_domingo':materias_aluno_domingo,
                'materias_aluno_segunda':materias_aluno_segunda,
                'materias_aluno_terca':materias_aluno_terca,
                'materias_aluno_quarta':materias_aluno_quarta,
                'materias_aluno_quinta':materias_aluno_quinta,
                'materias_aluno_sexta':materias_aluno_sexta,
                'materias_aluno_sabado':materias_aluno_sabado,
                'materias_aluno_logado':materias_aluno,
               'dias_semana': np.arange(1,8),
               'alunos': User.objects.all(),
               'form': form,
               'horarios':np.arange(len(materias_aluno)),
               }

    return render(request, 'perfil.html', context=context)

@user_passes_test(lambda u: u.is_superuser)
def add_materia_aluno(request):
    if request.method == 'POST':

        aluno = request.POST.get("aluno")
        materias = request.POST.getlist("materia")
        dias_semana = request.POST.getlist("dia_semana")
        horarios_iniciais = request.POST.getlist("horario_inicial")
        horarios_finais = request.POST.getlist("horario_final")
        
        print(list(zip(materias, dias_semana, horarios_iniciais, horarios_finais)))

        for materia, dia_semana, horario_inicial, horario_final in zip(materias, dias_semana, horarios_iniciais, horarios_finais):
            form = MateriaAlunoForm(data = {
                                            'aluno': User.objects.filter(id=aluno).first(),
                                            'materia': Materias.objects.filter(id=materia).first(),
                                            'dia_semana': dia_semana,
                                            'horario_inicial': horario_inicial,
                                            'horario_final': horario_final
                                            }
                                    )
            if form.is_valid():
                form.save()
        
        return render(request, 'add_materia_form.html', {'form': MateriaAlunoForm(), 'msg_sucess':'Registrado com sucesso!'})
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