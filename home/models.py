from django.db import models
from django.utils import timezone

class Confeiteiro(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.CharField(max_length=15)
    classificacao = models.CharField(max_length=20, default='A',
        choices=(
            ('A', '⭐⭐⭐⭐⭐'),
            ('B', '⭐⭐⭐⭐'),
            ('C', '⭐⭐⭐'),
            ('D', '⭐⭐'),
            ('E', '⭐'),
        )
    )

    def __str__(self):
        return self.nome

class Bolo(models.Model):
    sabor = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    data_fabricacao = models.DateTimeField(default=timezone.now())
    data_validade = models.DateTimeField(default=timezone.now())
    mostrar = models.BooleanField(default=True)
    confeiteiro = models.ForeignKey(Confeiteiro, on_delete=models.DO_NOTHING)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')

    def __str__(self):
        return self.sabor

