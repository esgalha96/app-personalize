from django import forms
from .models import User, MateriaAluno


class UserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Aluno", 
                                  widget=forms.Select(attrs={'onchange': 'submit()'}))

class MateriaAlunoForm(forms.ModelForm):

    class Meta:
        model = MateriaAluno
        fields = '__all__'
        widgets = {
            'aluno': forms.Select(attrs={'class':'form-control'}),
            'materia': forms.Select(attrs={'class':'form-control'}),
            'dia_semana': forms.Select(attrs={'class':'form-control'}),
            'horario_inicial': forms.Select(attrs={'class':'form-control'}),
            'horario_final': forms.Select(attrs={'class':'form-control'}),

        }


        
class MateriaAlunoDeleteAllForm(forms.Form):

    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Aluno")
