from django.test import TestCase
from django.shortcuts import resolve_url as r

#detecta as funcoes pela palavra test_
'''funcionamento. A classe HomeTest eh detectada e logo apos sao detectados na ordem os metodos que iniciam com test.
Apos detectar ele executa o metodo setUp -> test_get ->tearDown(so faz rollback), setUp --> test_template --> tearDown
'''
class HomeTest(TestCase): #testCase vem do django. Neste caso HomeTest(cenario de testegit sta) herda de TestCase.
    def setUp(self):
        self.response = self.client.get(r('home'))   #client realiza o teste funcional sem passar pela infraestrutura da rede. Vai para o django acessa a url, neste caso o '/' e pega a resposta

    def test_get(self):
        '''GET / must return status code 200'''
        self.assertEqual(200, self.response.status_code) #inspeciona a resposta

    def test_template(self):
        '''Must use index.html'''
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)