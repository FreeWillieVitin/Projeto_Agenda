from django.core.exceptions import ValidationError
from contato.models import Contato
from django import forms


class FormContato(forms.ModelForm):
    f_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o Primeiro Nome'
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda ao usuário'
    )
    # qualquer = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholders': 'Campo aleatório'
    #         }
    #     ),
    #     label='Só para teste'
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['f_name'].widget.attrs.update(
        #     {'placeholder': 'Digite o Primeiro Nome',
        #     }
        # )

    class Meta:
        model = Contato
        fields = (
            'f_name',
            'l_name',
            'telefone',
            'email',
            'descricao',
            'cod_categ'
        )
        # widgets = {
        #     'f_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Digite o Primeiro Nome',
        #             'name': 'Primeiro Nome'
        #         }
        #     )
        # }

    def clean(self):
        f_name = self.cleaned_data.get('f_name')
        l_name = self.cleaned_data.get('l_name')

        if f_name == l_name:
            msg = ValidationError(
                'Nome Iguais',
                code='invalid'
            )

            self.add_error(
                'f_name',
                msg
            )
            self.add_error(
                'l_name',
                msg
            )

        return super().clean()

    def clean_f_name(self):
        first_name = self.cleaned_data.get('f_name')

        if first_name == 'ABC':
            self.add_error(
                'f_name',
                ValidationError(
                    'Campo Inválido',
                    code='invalid'
                )
            )

        return first_name
