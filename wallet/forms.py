from django import forms


class WalletCreateForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nazwa'})
    )

