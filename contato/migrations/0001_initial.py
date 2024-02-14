# Generated by Django 4.2.7 on 2024-02-13 23:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(blank=True, max_length=50)),
                ('telefone', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('data_contato', models.DateTimeField(default=django.utils.timezone.now)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
    ]