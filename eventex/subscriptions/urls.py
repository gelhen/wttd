from django.conf.urls import url
from eventex.subscriptions.views import new, detail

urlpatterns = [
    url(r'^$', new, name='new'),  #quando o resto for vazio vai ser new
    url(r'^(\d+)/$', detail, name='detail'), # quando tiver o id e uma barra. \d+ pega um ou mais digitos dinamicamente url(r'^inscricao/1/$', detail),
]
