from django.apps import AppConfig


# Configurações do app, é da variável name que é retirado o nome a ser incluído na lista de Apps da core do projeto
class ContatoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contato'
