from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from wallet.forms import WalletCreateForm, CashFlowCreateForm, CashFlowUpdateForm, CashFlowCreateWalletForm
from wallet.models import Wallet, CashFlow


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

class WalletListView(LoginRequiredMixin, View):

    def get(self, request):
        wallets = Wallet.objects.filter(owner=request.user)
        return render(request, 'list.html', {'wallets': wallets})


class DeleteWalletView(UserPassesTestMixin, View):

    def test_func(self):
        user = self.request.user
        wallet = Wallet.objects.get(pk=self.kwargs['pk'])
        return wallet.owner == user


    def get(self, request, pk):
        wallet = Wallet.objects.get(pk=pk)
        return render(request, 'delete.html', {'wallet': wallet})

    def post(self, request, pk):
        operacja = request.POST.get('delete')
        if operacja == 'tak':
            wallet = Wallet.objects.get(pk=pk)
            wallet.delete()
        return redirect('list_wallet')


class CashFlowCreateView(LoginRequiredMixin, View):

    def get(self, request):
        form = CashFlowCreateForm(user=request.user)
        return render(request, 'form.html', {'form':form})


    def post(self, request):
        form = CashFlowCreateForm(request.POST, user=request.user)
        if form.is_valid():
            cf = form.save()
            return redirect('home')
        return render(request, 'form.html', {'form': form})


class WalletDetailView(UserPassesTestMixin, View):

    def test_func(self):
        user = self.request.user
        wallet = Wallet.objects.get(pk=self.kwargs['pk'])
        return wallet.owner == user

    def get(self, request, pk):
        wallet = Wallet.objects.get(pk=pk)
        form = CashFlowCreateWalletForm()
        return render(request, 'wallet.html', {'wallet': wallet, 'form':form})

    def post(self, request, pk):
        wallet = Wallet.objects.get(pk=pk)
        form = CashFlowCreateWalletForm(request.POST)
        if form.is_valid():
            cf = form.save(commit=False)
            cf.wallet = wallet
            cf.save()
            form.save_m2m()
            return redirect('detail_wallet', wallet.id)
        return render(request, 'wallet.html', {'wallet': wallet, 'form': form})


class CashFlowUpdateView(LoginRequiredMixin, View):

    def test_func(self):
        user = self.request.user
        cf = CashFlow.objects.get(pk=self.kwargs['pk'])
        return cf.wallet.owner == user

    def get(self, request, pk):
        cf = CashFlow.objects.get(pk=pk)
        form = CashFlowUpdateForm(instance=cf)
        return render(request, 'form.html', {'form': form})

    def post(self, request, pk):
        cf = CashFlow.objects.get(pk=pk)
        form = CashFlowUpdateForm(request.POST, instance=cf)
        if form.is_valid():
            form.save()
            return redirect('detail_wallet', cf.wallet.pk)
        return render(request, 'form.html', {'form': form})

