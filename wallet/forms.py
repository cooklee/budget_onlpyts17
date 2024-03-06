from django import forms
from django.core.exceptions import ValidationError


# def check_len(value):
#     if len(value) < 3:
#         raise ValidationError('Nazwa jest za krótka')
#
# def check_upper(value):
#     if not value[0].isupper():
#         raise ValidationError('Musi zaczynać sie wielką literą')
class WalletCreateForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa'}),
        # validators=[check_len, check_upper]
    )


