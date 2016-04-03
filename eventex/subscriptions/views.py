from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    '''
    Quando eh get mostra um formulario vazio e quando é post cria um formulario
    '''
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST) #pega informacoes que vem do post do request
    #form.full_clean() # pega os dados do formulario e retorno um dict dos dados

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form':form})

    subscription = Subscription.objects.create(**form.cleaned_data)

    #Send mail
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk = pk) # pega do banco de dados
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription':subscription})

def _send_mail(subject, from_, to, template_neme, context):
    body = render_to_string(template_neme, context)
    mail.send_mail(subject, body, from_, [from_, to ])