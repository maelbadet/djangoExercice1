from django.test import TestCase
from factures.models import Facture, Client

class FactureModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(nom="Client Test")

    def test_creer_facture(self):
        facture = Facture.objects.create(title="Facture Test", client=self.client)
        self.assertEqual(facture.title, "Facture Test")

    def test_client_facture(self):
        facture = Facture.objects.create(title="Facture Client", client=self.client)
        self.assertEqual(facture.client.nom, "Client Test")

    def test_facture_str(self):
        facture = Facture.objects.create(title="Facture STR", client=self.client)
        self.assertIn("Facture STR", str(facture))
