# Generated by Django 3.1.2 on 2021-01-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0002_auto_20201230_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alkoholfreiedrinks',
            name='zusatzstoffe',
            field=models.CharField(blank=True, default='', max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='hauptspeise',
            name='zusatzstoffe',
            field=models.CharField(blank=True, default='', max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='nachspeise',
            name='zusatzstoffe',
            field=models.CharField(blank=True, default='', max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='snacks',
            name='zusatzstoffe',
            field=models.CharField(blank=True, default='', max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='vorspeise',
            name='zusatzstoffe',
            field=models.CharField(blank=True, default='', max_length=55, null=True),
        ),
    ]