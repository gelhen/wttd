from unittest.mock import Mock

from django.test import  TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        #cria uma inscrição no banco
        Subscription.objects.create(name="Andre Marcos Gelhen", cpf="12345678901",
                                    email="gelhen@gmai.com", phone="49-88088808")
        #instancio o subscription model admin
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Action mark_as_paid should be installed"""
        self.assertIn('mark_as_paid', self.model_admin.actions)


    def test_mark_all(self):
        """It should mark all selected subscriptions as paid"""
        self.call_action()
        #verifico o resultado
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """It should send a message to the user."""
        mock = self.call_action()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

    def call_action(self):
        #montando uma query
        queryset = Subscription.objects.all()

        mock = Mock()
        #guardo o stado anterior
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        #chama a action passando o queryset
        self.model_admin.mark_as_paid(None, queryset)

        return mock

