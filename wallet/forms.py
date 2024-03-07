from django import forms
from django.core.exceptions import ValidationError

from wallet.models import CashFlow, Wallet


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


class CashFlowCreateForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wallet'].queryset = Wallet.objects.filter(owner=user)

    class Meta:
        model = CashFlow
        fields = "__all__"
        widgets = {
            'category': forms.CheckboxSelectMultiple,
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class CashFlowCreateWalletForm(forms.ModelForm):

    class Meta:
        model = CashFlow
        exclude = ['wallet']
        widgets = {
            'category': forms.CheckboxSelectMultiple,
            'date': forms.DateInput(attrs={'type': 'date'}),
            'type':forms.RadioSelect()
        }

class CashFlowUpdateForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        exclude = ['wallet', 'date', 'type']
        widgets = {
            'category': forms.CheckboxSelectMultiple
        }


