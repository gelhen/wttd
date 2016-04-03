from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    '''classe que vai gerir o relacionamento e o admin do django'''
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at',
                    'subscribed_today', 'paid') #colunas do change list
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('paid', 'created_at')

    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True


    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcadas como pagas.'

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'marcar como pago'

admin.site.register(Subscription, SubscriptionModelAdmin) #digo para o django que SubscriptionModelAdmin vai intermediar a relacao entre o modelo subscription e o  admin do django