from django.shortcuts import render

def password_change(request):
    context = {}
    return render(request, 'apacheauth/password_change.html', context)

