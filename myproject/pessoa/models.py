from django.db import models

class Pessoa(models.Model):

    nome_pessoa = models.CharField(max_length=100, db_column='nome')
    data_nasc_pessoa = models.DateField(db_column='data_nasc')
    cpf_pessoa = models.CharField(max_length=14, unique=True, db_column='cpf')
    sexo_pessoa = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='sexo')
    altura_pessoa = models.FloatField(db_column='altura')
    peso_pessoa = models.FloatField(db_column='peso')

    def __str__(self):
        return self.nome_pessoa
