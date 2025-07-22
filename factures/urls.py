from django.urls import path

from . import views
from .views import ProduitListView, ProduitDetailView, ProduitUpdateView, ProduitCreateView, ProduitDeleteView

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:facture_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
	# Catégories
	path('categories/', views.CategorieListView.as_view(), name='categorie_list'),
	path('categories/new/', views.CategorieCreateView.as_view(), name='categorie_create'),
	path('categories/<int:pk>/', views.CategorieDetailView.as_view(), name='categorie_detail'),
	path('categories/<int:pk>/edit/', views.CategorieUpdateView.as_view(), name='categorie_update'),
	path('categories/<int:pk>/delete/', views.CategorieDeleteView.as_view(), name='categorie_delete'),

	# Produits
	path('produits/', views.ProduitListView.as_view(), name='produit_list'),
	path('produits/new/', views.ProduitCreateView.as_view(), name='produit_create'),
	path('produits/<int:pk>/', views.ProduitDetailView.as_view(), name='produit_detail'),
	path('produits/<int:pk>/edit/', views.ProduitUpdateView.as_view(), name='produit_update'),
	path('produits/<int:pk>/delete/', views.ProduitDeleteView.as_view(), name='produit_delete'),

	# Commandes
	path('commandes/', views.CommandeListView.as_view(), name='commande_list'),
	path('commandes/new/', views.CommandeCreateView.as_view(), name='commande_create'),
	path('commandes/<int:pk>/', views.CommandeDetailView.as_view(), name='commande_detail'),
	path('commandes/<int:pk>/edit/', views.CommandeUpdateView.as_view(), name='commande_update'),
	path('commandes/<int:pk>/delete/', views.CommandeDeleteView.as_view(), name='commande_delete'),

	# Factures
	path('factures/', views.FactureListView.as_view(), name='facture_list'),
	path('factures/new/', views.FactureCreateView.as_view(), name='facture_create'),
	path('factures/<int:pk>/', views.FactureDetailView.as_view(), name='facture_detail'),
	path('factures/<int:pk>/edit/', views.FactureUpdateView.as_view(), name='facture_update'),
	path('factures/<int:pk>/delete/', views.FactureDeleteView.as_view(), name='facture_delete'),
]