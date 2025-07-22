from typing import Any

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from decimal import Decimal

from .forms import ProduitForm, CategorieForm, CommandeForm, FactureForm, CommandeProduitFormSet
from .models import Produit, Categorie, Commande, Facture

def home(request):
    return render(request, 'factures/index.html')
def index(request):
    latest_product_list = Produit.objects.order_by("-created_at")[:5]
    context = {"latest_product_list": latest_product_list}
    return render(request, "factures/index.html", context)


def detail(request, facture_id):
    Produits = get_object_or_404(Produit, pk=facture_id)
    return render(request, "factures/detail.html", {"produit": Produits})


# CRUD pour les categories

class CategorieListView(ListView):
    model = Categorie
    template_name = 'factures/categories/category_list.html'


class CategorieDetailView(DetailView):
    model = Categorie
    template_name = 'factures/categories/category_detail.html'


class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'factures/categories/category_form.html'
    success_url = reverse_lazy('categorie_list')


class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'factures/categories/category_form.html'
    success_url = reverse_lazy('categorie_list')


class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = 'factures/categories/category_confirm_delete.html'
    success_url = reverse_lazy('categorie_list')


# CRUD pour les produits
class ProduitListView(ListView):
    model = Produit
    template_name = 'factures/produits/produit_list.html'


class ProduitDetailView(DetailView):
    model = Produit
    template_name = 'factures/produits/produit_detail.html'


class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'factures/produits/produit_form.html'
    success_url = reverse_lazy('produit_list')


class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'factures/produits/produit_form.html'
    success_url = reverse_lazy('produit_list')


class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'factures/produits/produit_confirm_delete.html'
    success_url = reverse_lazy('produit_list')


### COMMANDE ###
class CommandeListView(ListView):
    model = Commande
    template_name = 'factures/commandes/commande_list.html'


class CommandeDetailView(DetailView):
    model = Commande
    template_name = 'factures/commandes/commande_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #recup le context existant
        commande = self.get_object() #recupere l'instance de l'objet

        total_ht = 0
        total_ttc = 0
        lignes = []

        for item in commande.commande_produits.all():
            prix_ht = item.produit.price
            prix_ttc = prix_ht + (prix_ht * Decimal(item.produit.tva) / Decimal("100"))
            quantite = item.quantite
            ligne_ht = prix_ht * quantite
            ligne_ttc = prix_ttc * quantite

            total_ht += ligne_ht
            total_ttc += ligne_ttc

            lignes.append({
                "produit": item.produit,
                "quantite": quantite,
                "prix_ht": prix_ht,
                "prix_ttc": prix_ttc,
                "ligne_ht": ligne_ht,
                "ligne_ttc": ligne_ttc,
            })

        context["lignes"] = lignes
        context["total_ht"] = total_ht
        context["total_ttc"] = total_ttc
        context["difference"] = total_ttc - total_ht
        return context


class CommandeCreateView(CreateView):
    model = Commande
    form_class = CommandeForm
    template_name = 'factures/commandes/commande_form.html'
    success_url = reverse_lazy('commande_list')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        formset = CommandeProduitFormSet()
        return render(request, self.template_name, {'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        formset = CommandeProduitFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            commande = form.save()
            formset.instance = commande
            formset.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'formset': formset})

class CommandeUpdateView(UpdateView):
    model = Commande
    form_class = CommandeForm
    template_name = 'factures/commandes/commande_form.html'
    success_url = reverse_lazy('commande_list')


class CommandeDeleteView(DeleteView):
    model = Commande
    template_name = 'factures/commandes/commande_confirm_delete.html'
    success_url = reverse_lazy('commande_list')


### FACTURE ###
class FactureListView(ListView):
    model = Facture
    template_name = 'factures/factures/facture_list.html'


class FactureDetailView(DetailView):
    model = Facture
    template_name = 'factures/factures/facture_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        facture = self.object

        commandes_details = []
        total_ht_facture = Decimal('0.00')
        total_ttc_facture = Decimal('0.00')

        for commande in facture.commandes.all():
            total_ht_commande = Decimal('0.00')
            total_ttc_commande = Decimal('0.00')
            produits_details = []

            # On suppose que CommandeProduit est la table intermédiaire entre Commande et Produit
            for ligne in commande.commande_produits.all():
                prix_ht = ligne.produit.price
                tva = ligne.produit.tva
                quantite = ligne.quantite

                prix_ttc = prix_ht + (prix_ht * Decimal(tva) / Decimal("100"))
                ligne_ht = prix_ht * quantite
                ligne_ttc = prix_ttc * quantite

                total_ht_commande += ligne_ht
                total_ttc_commande += ligne_ttc

                produits_details.append({
                    'produit': ligne.produit,
                    'prix_ht': prix_ht,
                    'tva': tva,
                    'prix_ttc': prix_ttc,
                    'quantite': quantite,
                    'ligne_ht': ligne_ht,
                    'ligne_ttc': ligne_ttc,
                })

            commandes_details.append({
                'commande': commande,
                'produits': produits_details,
                'total_ht_commande': total_ht_commande,
                'total_ttc_commande': total_ttc_commande,
            })

            total_ht_facture += total_ht_commande
            total_ttc_facture += total_ttc_commande

        context['commandes_details'] = commandes_details
        context['total_ht_facture'] = total_ht_facture
        context['total_ttc_facture'] = total_ttc_facture
        context['total_tva_facture'] = total_ttc_facture - total_ht_facture

        return context


class FactureCreateView(CreateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/factures/facture_form.html'
    success_url = reverse_lazy('facture_list')


class FactureUpdateView(UpdateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/factures/facture_form.html'
    success_url = reverse_lazy('facture_list')


class FactureDeleteView(DeleteView):
    model = Facture
    template_name = 'factures/factures/facture_confirm_delete.html'
    success_url = reverse_lazy('facture_list')
