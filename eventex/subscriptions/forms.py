from django import forms
from django.core.exceptions import ValidationError

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('Cpf deve conter apenas númereos.', 'digits')

    if len(value) != 11:
        raise ValidationError('Cpf deve ter 11 números.', 'length')

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='Cpf', validators=[validate_cpf])
    email = forms.EmailField(label='E-mail', required=False) #por padrao todo campo é  requerido
    phone = forms.CharField(label='Telefone', required=False)

    # clean_xxxxxxx é um metodo complementar que a validação do formulario chama. Sempre vai ser clean_[campo existente]
    # ele é disparado depois do clean do CharField
    def clean_name(self):
        name = self.cleaned_data['name'] #metodo disparado pelo CharField

        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    #meto do form. Ele é chamado depois que todos os campos foram carregados.
    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')
        #sempre que o clean do formulario for implementado tem que retornar um dicionario com todos os clean data do form
        #se retornar None vai sobstituir o cleaned_data existente
        return self.cleaned_data