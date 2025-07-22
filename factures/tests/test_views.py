from django.test import TestCase
from django.urls import reverse
from factures.models import Facture, Client

class FactureViewTests(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(nom="Client Test")
        self.facture = Facture.objects.create(title="Facture Vue", client=self.client_obj)

    def test_facture_list_view_status_code(self):
        response = self.client.get(reverse("facture_list"))
        self.assertEqual(response.status_code, 200)

    def test_facture_list_view_context(self):
        response = self.client.get(reverse("facture_list"))
        self.assertIn("object_list", response.context)

    def test_facture_detail_view(self):
        response = self.client.get(reverse("facture_detail", args=[self.facture.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.facture.title)

    def test_facture_create_view_get(self):
        response = self.client.get(reverse("facture_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nouvelle facture")

    def test_facture_create_post(self):
        data = {
            "title": "Nouvelle facture post",
            "client": self.client_obj.id,
        }
        response = self.client.post(reverse("facture_create"), data)
        self.assertEqual(response.status_code, 302)  # Redirection après succès
        self.assertTrue(Facture.objects.filter(title="Nouvelle facture post").exists())
