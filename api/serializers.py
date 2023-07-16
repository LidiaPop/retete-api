from rest_framework import serializers
from . models import Reteta, Ingredient, Meniu


class ListIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'nume')


class RetetaSerializer(serializers.ModelSerializer):
    ingrediente = ListIngredienteSerializer(many=True)

    class Meta:
        model = Reteta
        fields = ('id', 'nume', 'ingrediente', 'timp_preparare', 'portii', 'timp_preparare_minute')


class RetetaMeniuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reteta
        fields = ('id','nume',  'timp_preparare_minute')


class MeniuSerializer(serializers.ModelSerializer):
    aperitiv = RetetaMeniuSerializer()
    fel_principal = RetetaMeniuSerializer()
    desert = RetetaMeniuSerializer()
    total_portii = serializers.SerializerMethodField()


    class Meta:
        model = Meniu
        fields = ('id', 'nume', 'aperitiv', 'fel_principal', 'desert', 'total_portii')

    def get_total_portii(self, meniu):
        return meniu.aperitiv.portii + meniu.fel_principal.portii + meniu.desert.portii

