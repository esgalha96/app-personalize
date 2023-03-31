from django.db import models
from django.contrib.auth.models import User

FRENTES_MATERIAS = (
    ('I','I'),
    ('II', 'II'),
    ('III','III'),
    ('IV','IV'),
    ('V','V'),
)

DIA_SEMANA = (
    (1,'Domingo'),
    (2,'Segunda-feira'),
    (3,'Terça-feira'),
    (4,'Quarta-feira'),
    (5,'Quinta-feira'),
    (6,'Sexta-Feira'),
    (7,'Sábado'),
)

HORARIOS_AULA = (
    ('07:00','07:00'),
    ('07:30','07:30'),
    ('08:00','08:00'),
    ('08:30','08:30'),
    ('09:00','09:00'),
    ('09:30','09:30'),
    ('10:00','10:00'),
    ('10:30','10:30'),
    ('11:00','11:00'),
    ('11:30','11:30'),
    ('12:00','12:00'),
    ('12:30','12:30'),
    ('13:00','13:00'),
    ('13:30','13:30'),
    ('14:00','14:00'),
    ('14:30','14:30'),
    ('15:00','15:00'),
)

class Materias(models.Model):

    nome_materia = models.CharField(max_length=50, verbose_name="Matéria")
    frente_materia = models.CharField(max_length=3, choices=FRENTES_MATERIAS, default='I')

    def __str__(self):
        return self.nome_materia + " " + self.frente_materia
    
    class Meta:
        ordering = ['nome_materia', 'frente_materia']

class MateriaAluno(models.Model):

    aluno = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Aluno")
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE, verbose_name="Matéria")
    dia_semana = models.IntegerField(choices=DIA_SEMANA, default=2, verbose_name="Dia da Semana")
    horario_inicial = models.CharField(max_length=5, choices=HORARIOS_AULA, default="07:00", verbose_name="Horário Inicial")
    horario_final = models.CharField(max_length=5, choices=HORARIOS_AULA, default="07:30", verbose_name="Horário Final")
    
    def __str__(self):
        return str(self.aluno.first_name) + " - " + str(self.materia) + " (" + str(self.horario_inicial) + " às " + str(self.horario_final) + ")"
        
    class Meta:
        ordering = ["horario_inicial", "materia"]
