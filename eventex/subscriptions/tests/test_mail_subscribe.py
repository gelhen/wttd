from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Andre Marcos Gelhen', cpf='12345678901', email='gelhen@gmail.com', phone='49 88009911')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

   #testa a formatacao do email
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    #testa o remetente
    def test_subscription_email_from(self):
        expect = 'gelhen@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    #testa o destinatario
    def test_subscription_email_to(self):
        expect = ['gelhen@gmail.com','gelhen@gmail.com']

        self.assertEqual(expect, self.email.to)

    #testa o corpo do email
    def test_subscription_email_body(self):
        contents = [
            'Andre Marcos Gelhen',
            '12345678901',
            'gelhen@gmail.com',
            '49 88009911'
        ]


    #valida o que o esta sendo enviado no formulario e mostra o que esta faltando