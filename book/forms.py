from django import forms
from django.core.exceptions import ValidationError

from book.models import Book


def check_button(value):
    if value != 'Tak':
        raise ValidationError('')

class BookDeleteForm(forms.Form):
    action = forms.CharField(validators=[check_button])


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['year'] < cleaned_data['author'].year:
            raise ValidationError('wydanie książki nie moze być przed urodzeniem autora')
        return cleaned_data

