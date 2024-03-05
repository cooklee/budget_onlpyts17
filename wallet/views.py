from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from wallet.forms import WalletCreateForm
from wallet.models import Wallet


# Create your views here.
class WalletCreateView(LoginRequiredMixin, View):

    def get(self, request):

        form = WalletCreateForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        user = request.user
        form = WalletCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Wallet.objects.create(owner=user, name=name)
            return redirect('home')
        return render(request, 'form.html', {'form': form})

