# Generated by Django 3.1.2 on 2020-12-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0002_besucher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alkoholfreiedrinks',
            name='preis',
            field=models.DecimalField(decimal_places=2, default=600.0, max_digits=8, max_length=8),
        ),
        migrations.AlterField(
            model_name='alkoholhaltigedrinks',
            name='preis',
            field=models.DecimalField(decimal_places=2, default=600.0, max_digits=8, max_length=8),
        ),
        migrations.AlterField(
            model_name='hauptspeise',
            name='preis',
            field=models.DecimalField(decimal_places=2, default=600.0, max_digits=8, max_length=8),
        ),
        migrations.AlterField(
            model_name='nachspeise',
            name='preis',
            field=models.DecimalField(decimal_places=2, default=600.0, max_digits=8, max_length=8),
        ),
        migrations.AlterField(
            model_name='snacks',
            name='preis',
            field=models.DecimalField(decimal_places=2, default=600.0, max_digits=8, max_length=8),
        ),
        migrations.AlterField(
            model_name='vorspeise',
            name='preis',
            field=models.DecimalField(decimal_places=2, default=600.0, max_digits=8, max_length=8),
        ),
    ]
