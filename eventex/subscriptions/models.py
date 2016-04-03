from django.db import models


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        '''Impletmenta algumas configuracoes genericas que o django permite '''
        verbose_name_plural = 'inscrições' # altera o nome de subscriptions para inscrições
        verbose_name        = 'inscricao'
        ordering = ('-created_at', ) # o hifem indica ordem decrescente

    def __str__(self):
        '''eh o protocolo do python para dizer o que acontece com qualque objeto python quando eu instancio uma string apartit dele'''
        return  self.name