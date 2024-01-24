from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    

class Car(models.Model):  # Classe Car com herança da biblioteca models
    # autofield para auto preencher e primake_jey para ser a primeira coisa da tabela
    id = models.AutoField(primary_key=True)
    # charfield, um campo de caracteres e pode ter no max 200
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') #ForeignKey fiz que será uma ligação a outra tabela, on_delete no modo Protect = não deixa deletar e related_name é como irá chamar o nome da relação entre as dus tabela
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True) #Adição de placas dos carros que podem ficar com informação nula e em branco
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) #Campo de imagem e ele vai armazenar essa foto na pasta cars/

    def __str__(self):
        return self.model

