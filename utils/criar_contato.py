import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contato.models import Categoria, Contato

    # Contato.objects.all().delete()
    # Categoria.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Conhecidos', 'Empresas']

    django_categories = [Categoria(desc_categ=desc_categ)
                         for desc_categ in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        f_name, l_name = profile['name'].split(' ', 1)
        telefone = fake.phone_number()
        data_contato: datetime = fake.date_this_year()
        descricao = fake.text(max_nb_chars=100)
        cod_categ = choice(django_categories)

        django_contacts.append(
            Contato(
                f_name=f_name,
                l_name=l_name,
                telefone=telefone,
                email=email,
                data_contato=data_contato,
                descricao=descricao,
                cod_categ=cod_categ,
            )
        )

    if len(django_contacts) > 0:
        Contato.objects.bulk_create(django_contacts)
