from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect


def nicht_authentifizierter_user(view_func):
    '''
        Decorater der eine View-Funktion verarbeitet

                Parameters:
                        view_func (Function): Eine View-Funktion

                Returns:
                        wrapper_func(): Gibt die Wrapper-Funktion zurück

    '''
    def wrapper_func(request, *args, **kwargs):
        '''
            Der User soll zurück zum Dashboard kommen wenn er eingeloggt ist und versucht, auf die Login-Seite zu kommen

                    Parameters:
                            request (HttpRequest): Ein Request-Object

                    Returns:
                            redirect(): Leitet den User zum Dashboard weiter
                            view_func(): Die eigentliche Funktion die ausgeführt werden soll, falls der User noch nicht
                            eingeloggt ist

        '''
        if request.user.is_authenticated:
            return redirect('crm_dashboard')
            pass
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def genehmigte_user(allowed_roles=[]):
    '''
        Hilfsmethode, um die Liste als Input zu haben

                Parameters:
                        allowed_roles (list): Liste mit den Gruppen

                Returns:
                        decorater(): Der eigentliche Decorater

    '''
    def decorater(view_func):
        '''
            Decorater der eine View-Funktion verarbeitet

                    Parameters:
                            view_func (Function): Eine View-Funktion

                    Returns:
                            decorater(): Gibt die Wrapper-Funktion zurück

        '''
        def wrapper_func(request, *args, **kwargs):
            '''
                Falls die Gruppe des Users erlaubt wird, wird die View-Funktion ausgeführt, falls er ein Kunde ist
                wird er zum Kundendashboard weitergeleitet und falls der User keiner Gruppe zugehört, kriegt er die
                Warnngsmeldung

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                view_func(): Die eigentliche View-Funktion
                                redirect(): Man wird zum Kundendashboard weitergeleitet
                                HttpResponse(): Warnung aufgrund unerlaubten Zugriffs

            '''
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            elif group == 'kunde':
                return redirect("menucard_dashboard")
            else:
                return HttpResponse(
                    'Sie haben keine Befugnis für diese Seite. <b>Schließen Sie das Fenster.</b>'
                    '<script>alert("Sie haben kein Zugriff auf diese Seite");</script>'
                )

        return wrapper_func

    return decorater
