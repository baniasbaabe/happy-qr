# Generated by Django 3.1.2 on 2020-11-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alkoholfreiedrinks',
            name='beschreibung',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='alkoholhaltigedrinks',
            name='beschreibung',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='hauptspeise',
            name='beschreibung',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='nachspeise',
            name='beschreibung',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='snacks',
            name='beschreibung',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='vorspeise',
            name='beschreibung',
            field=models.TextField(blank=True, default=''),
        ),
    ]
