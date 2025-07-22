from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.EmailField()
    telephone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # pour soft-delete

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Categorie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Produit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.FloatField()
    quantity = models.PositiveIntegerField() #on ne commande pas un produit avec -3 quantite
    category = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Commande(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class CommandeProduit(models.Model):
    commande = models.ForeignKey("Commande", on_delete=models.CASCADE, related_name="commande_produits")
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

class Facture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    commandes = models.ManyToManyField('Commande', blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    paye = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.categorie:
            autres, _ = Categorie.objects.get_or_create(title="Autres", defaults={"description": "Catégorie par défaut"})
            self.categorie = autres
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
