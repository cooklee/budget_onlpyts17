from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from book.models import Author, Book
from django import forms


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


# Create your views here.
class CreateAuthorView(CreateView):
    model = Author
    form_class =CreateAuthorForm
    success_url = reverse_lazy('home')
    template_name = 'form.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context

class ListBookView(ListView):
    model = Author
    template_name = 'list.html'

    def get_queryset(self):
        super(ListBookView, self).get_queryset()


class DetailAuthorView(DetailView):
    model = Author
    template_name = 'book_detail.html'

    def get_object(self, queryset=None):
        super().get_object()

class UpdateAuthorView(UpdateView):
    model = Author
    form_class = CreateAuthorForm
    success_url = reverse_lazy('home')
    template_name = 'form.html'


class DeleteAuthorView(DeleteView):
    model = Author
    success_url = reverse_lazy('home')
    template_name = 'form.html'
