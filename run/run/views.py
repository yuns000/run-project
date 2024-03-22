from django.shortcuts import redirect


def goto_login(request):
    return redirect('accounts:login')