# Generated by Django 4.2.7 on 2024-02-15 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contato', '0005_remove_contato_cod_categ'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='cod_categ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contato.categoria'),
        ),
        migrations.AddField(
            model_name='contato',
            name='proprietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
