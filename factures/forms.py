from django import forms
from django.forms.models import inlineformset_factory

from .models import Client, Categorie, Produit, Commande, Facture, CommandeProduit


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
        exclude = ('deleted_at',)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('deleted_at',)

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'
        exclude = ('deleted_at',)

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
        exclude = ('deleted_at',)

CommandeProduitFormSet = inlineformset_factory(
    Commande,
    CommandeProduit,
    fields=('produit', 'quantite'),
    extra=1,
    can_delete=True
)

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = '__all__'
        exclude = ('deleted_at',)
