# Generated by Django 3.1.2 on 2020-12-06 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auftrag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produkt', models.CharField(choices=[('Digital Menucard', 'Digital Menucard')], default='Digital Menucard', max_length=45)),
                ('status', models.CharField(choices=[('Eingegangen', 'Eingegangen'), ('In Bearbeitung', 'In Bearbeitung'), ('Abgeschlossen', 'Abgeschlossen')], default='Eingegangen', max_length=45)),
                ('auftrag_vom', models.DateTimeField(auto_now_add=True, null=True)),
                ('preis', models.FloatField(default=600.0)),
                ('notiz', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=45)),
                ('nachname', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefon', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('web', models.CharField(blank=True, max_length=200, null=True)),
                ('notiz', models.TextField(blank=True, null=True)),
                ('template', models.CharField(choices=[('Template 1', 'Template 1'), ('Template 2', 'Template 2'), ('Template 3', 'Template 3')], default='Template 1', max_length=20)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mitarbeiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=45)),
                ('nachname', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Rechnung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(auto_now_add=True)),
                ('auftrag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.auftrag')),
                ('kunde', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.kunde')),
            ],
        ),
        migrations.AddField(
            model_name='auftrag',
            name='kunde',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.kunde'),
        ),
    ]
