# Eventex

Sistema de eventos encomendado pela morena
[![Build Status](https://travis-ci.org/gelhen/wttd.svg?branch=master)](https://travis-ci.org/gelhen/wttd)

## Como desenvolver?

1. Clone o repositorio.
2. Crie um vertualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os tests.

```console
git clone git@github.com:henriquebastosgisteventex.git wttd
cd wttd
python -m venv .wttd 
source .wttd\Scripts\activage.bat
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma instancia no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instancia
4. Defina DEBUG_FALSE=False
5. Configure o serviço de emais.
6. Envie o codigo para o HEROKU.

```console
heroku create mihainstancia
heroku config:push
heroku config:set SECRET_KEY=  f #endereço  hbn.link/secret_gen
heroku config: set DEBUB=False
#configura o email
git push heroku master --force'
```