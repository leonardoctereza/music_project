from django.db import models



class Banda(models.Model):
    nome = models.CharField(max_length=50)
    musicos = models.ManyToManyField('Musico')
    estilo = models.ForeignKey('EstiloMusical', on_delete = models.CASCADE)
    dataCriacao = models.DateField(auto_now_add = False)
    def __str__(self):
        return self.nome

class Musico(models.Model):
    nome = models.CharField(max_length=50)
    dataNascimento = models.DateField()
    nacionalidade = models.TextField()

    def __str__(self):
        return self.nome

class EstiloMusical(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
