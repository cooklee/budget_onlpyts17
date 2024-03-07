from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from book.forms import BookDeleteForm, BookCreateForm
from book.models import Author, Book
from django import forms
from django.contrib import messages

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


# Create your views here.
class CreateAuthorView(CreateView):
    model = Author
    form_class =CreateAuthorForm
    success_url = reverse_lazy('add_author')
    template_name = 'form.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context

class ListBookView(ListView):
    model = Author
    template_name = 'list.html'


class CreateBookView(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('create_book')

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
    success_url = reverse_lazy('add_author')
    template_name = 'delete_author.html'
    form_class = BookDeleteForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.info(self.request, f"udało sie usunąć: autora {self.object}")
        return response

    def form_invalid(self, form):
        return redirect('add_author')
