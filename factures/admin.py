from django.contrib import admin
from .models import Client, Categorie, Facture, Produit, Commande, CommandeProduit

@admin.action(description="Marquer comme payé")
def marquer_comme_paye(modeladmin, request, queryset):
    queryset.update(paye=True)

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    search_fields = ['title', 'client__nom']  # Permet de chercher par titre et nom de client
    list_filter = ['paye', 'client']          # Filtres dans la sidebar
    actions = [marquer_comme_paye]

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    search_fields = ['title', 'price','quantity']  # Permet de chercher par titre, prix et quantite

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['nom','prenom','mail'] # Permet de chercher par nom, prenom et mail

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    search_fields = ['title'] # Permet de chercher par titre

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    search_fields = ['title','client__nom'] # Permet de chercher par titre de commande ou nom client
    list_filter = ['client']

@admin.register(CommandeProduit)
class CommandeProduitAdmin(admin.ModelAdmin):
    search_fields = ['commande__title','produit__title','quantity'] # Permet de chercher par titre (commande, produit) et quantite
