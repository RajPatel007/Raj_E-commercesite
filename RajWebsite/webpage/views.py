from django.shortcuts import render


def home(request):
    return render(request, 'webpage/home.html')


def account(request):
    return render(request, 'webpage/account.html')


def deals(request):
    return render(request, 'webpage/deals.html')


def help(request):
    return render(request, 'webpage/help.html')


def registry(request):
    return render(request, 'webpage/registry.html')


def sell(request):
    return render(request, 'webpage/sell.html')
