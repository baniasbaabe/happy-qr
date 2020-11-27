from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect


def nicht_authentifizierter_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('crm_dashboard')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def genehmigte_user(allowed_roles=[]):
    def decorater(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    'Sie haben keine Befugnis für diese Seite. <b>Schließen Sie das Fenster.</b>'
                    '<script>alert("Sie haben kein Zugriff auf diese Seite");</script>'
                )

        return wrapper_func

    return decorater


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'admin':
                return view_func(request, *args, **kwargs)

            if group == 'mitarbeiter':
                return redirect('crm_dashboard')

            if group == 'kunde':
                return redirect('menucard_dashboard')

    return wrapper_func
