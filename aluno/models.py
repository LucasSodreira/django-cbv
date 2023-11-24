from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Quarto(models.Model):
    apartamento = models.IntegerField(("Número do apartamento"))
    valor = models.FloatField(("Valor da diária"))
    
    def __str__(self):
        return f"Quarto {self.apartamento}"
    
class Hospedagem(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    valor = models.FloatField(("Valor da hospedagem"))
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.data_saida < self.data_entrada:
            self.valor = 0  # ou outra lógica desejada para lidar com datas inválidas
        else:
            # Atualizar o valor da hospedagem quando um quarto é atribuído
            self.valor = self.quarto.valor * (self.data_saida - self.data_entrada).days
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.cliente} - {self.quarto} - {self.data_entrada} a {self.data_saida}"
    
class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    valor = models.FloatField(("Valor do consumo"))
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)
    
    

# class Cidade(models.Model):
#     nome = models.CharField(max_length=100)
#     sigla_estado = models.CharField(max_length=2)

#     def __str__(self):
#         return self.nome + " - " + self.sigla_estado 

# class Curso(models.Model):
#     nome = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome 

# class Aluno(models.Model):
#     nome_aluno = models.CharField(max_length=150)
#     endereco = models.CharField(max_length=250)
#     email = models.EmailField()
#     cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
#     curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

