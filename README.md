# Happy-QR

Happy-QR ist eine Webapplikation, die Gastronomen eine Webanwendung zur Verfügung stellt. Anhand dieser Webanwendung hat der Gastronom die Möglichkeit für sein Lokal digitale Menükarte zu erstellen und die digitale Covid-19 Datenerfassung einzurichten und seinen Kunden als QR-Code zur Verfügung zu stellen, damit diese den QR-Code mit dem Smartphone scannen und die Menükarte nutzen zu können bzw. sich im Lokal für die Covid-19 Nachverfolgung einzutragen. Der Gastronom kann seine digitale Menükarte optisch und inhaltlich ändern. Die erfassten Daten der Lokalbesucher kann der Gastronom auf Anfrage von Behörden ausdrucken bzw. den Behörden in elektronischer Form zukommen lassen.

Der Happy-QR Mitarbeiter kann über die integrierte CRM Webanwendung sämtliche Aufträge und Rechnungen von Gastronomen erfassen, bearbeiten, exportieren und ggf. löschen. Zudem besteht die Möglichkeit die Daten bzw. Dokumente als CSV oder PDF Datei zu exportieren. Darüber hinaus können Kundendaten gepflegt werden. 

Anwendung starten (Voraussetzung: Python auf dem Rechner):

Für Windows:
$ pip install virtualenv
$ py -m venv venv
$ venv\Scripts\activate
$ git clone https://github.com/baniasbaabe/happy-qr.git
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py test
$ python manage.py runserver

Über den Webbrowser auf localhost:8000 gehen
