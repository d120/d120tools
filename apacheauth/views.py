from django.shortcuts import render

def account_info(request):
    return render(request, 'apacheauth/account.html', {})

def password_change(request):
    context = {}
    return render(request, 'apacheauth/password_change.html', context)

def index(request):
    return render(request, 'apacheauth/index_view.html', {})
