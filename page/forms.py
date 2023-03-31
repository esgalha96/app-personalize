from django import forms
from .models import User, MateriaAluno


class UserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Aluno", 
                                  widget=forms.Select(attrs={'onchange': 'submit()'}))

class MateriaAlunoForm(forms.ModelForm):

    class Meta:
        model = MateriaAluno
        fields = '__all__'

class MateriaAlunoDeleteAllForm(forms.Form):

    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Aluno")
