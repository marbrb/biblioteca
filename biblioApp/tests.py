from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class Test(TestCase):
    def testViews(self):
        res = self.client.get(reverse('meta'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('buscar'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('contactos'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('gracias'))
        self.assertEqual(res.status_code, 200)

    def testContactos(self):
        data = {'asunto':'test asunto', 'mensaje': 'test mensaje'}
        res = self.client.post(reverse('contactos'), data)
        self.assertEqual(res.status_code, 302)
