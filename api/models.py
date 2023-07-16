from django.db import models


class Ingredient(models.Model):
    nume = models.CharField(max_length=128)

    def __str__(self):
        return self.nume

class Reteta(models.Model):
    nume = models.CharField(max_length=128)
    ingrediente = models.ManyToManyField(Ingredient)
    timp_preparare = models.IntegerField()
    portii = models.IntegerField()

    def timp_preparare_minute(self):
        return "{} minute".format(self.timp_preparare)
    def __str__(self):
        return self.nume


class Meniu(models.Model):
    nume = models.CharField(max_length=128)
    aperitiv = models.ForeignKey(Reteta, null=True, on_delete=models.SET_NULL, related_name='reteta_aperitive')
    fel_principal = models.ForeignKey(Reteta,null=True, on_delete=models.SET_NULL, related_name='reteta_feluri_principale')
    desert = models.ForeignKey(Reteta,  null=True,on_delete=models.SET_NULL, related_name='reteta_deserturi')

    def __str__(self):
        return self.nume
