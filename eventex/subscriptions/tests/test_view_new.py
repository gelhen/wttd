from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:new'))
    def test_get(self):
        '''Get /inscricao/ must return status code 200'''
        self.assertEqual(200, self.resp.status_code)
    def test_template(self):
        '''Must use subscriptions/subscription_form.html'''
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
    def test_html(self):
        '''Html must contais input tags'''
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        '''Html must contail csrf'''
        ''' ao incluir {% csrf_token %} no formuladio ajustar o teste de input para +1 pois este token gera um input escondido no formulario'''
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''Context must have subscription form'''
        '''Eh no contex que ficam as variaveis dinamicas'''
        form =  self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscriptionsNewGetPostValid(TestCase):
    def setUp(self):
        data = dict(name='Andre Marcos Gelhen', cpf='12345678901', email='gelhen@gmail.com', phone='49 88009911')
        self.resp = self.client.post(r('subscriptions:new'), data)


    def test_post(self):
        '''Valid POST should redirect to /inscricao/1/'''
        #302 eh o codigo do redirect
        self.assertRedirects(self.resp, r('subscriptions:detail', 1))

    def test_send_subscribe_email(self):
        #em teste o django nao envia email
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())

    #valida o que o esta sendo enviado no formulario e mostra o que esta faltando


class SubscriptionsNewGetPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        '''Invalid POST should not redirect'''
        self.assertEqual(200 , self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_forms_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def  test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

#Mostra erros do formulario
class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(name='Andre Marcos Gelhen', cpf='12345678901')
        response = self.client.post(r('subscriptions:new'), invalid_data)

        self.assertContains(response, '<ul class="errorlist nonfield">')

''' @unittest.skip('To be removed') #pula o teste abaixo
class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict (name='Andre Marcos Gelhen', cpf='12345678901',
                     email='gelhen@gmail.com', phone='49 88009911')

        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!') '''