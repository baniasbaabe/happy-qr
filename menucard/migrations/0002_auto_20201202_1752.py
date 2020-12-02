# Generated by Django 3.1.2 on 2020-12-02 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20201202_1752'),
        ('menucard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alkoholfreiedrinks',
            name='kundeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.kunde'),
        ),
        migrations.AddField(
            model_name='alkoholhaltigedrinks',
            name='kundeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.kunde'),
        ),
        migrations.AddField(
            model_name='hauptspeise',
            name='kundeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.kunde'),
        ),
        migrations.AddField(
            model_name='nachspeise',
            name='kundeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.kunde'),
        ),
        migrations.AddField(
            model_name='snacks',
            name='kundeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.kunde'),
        ),
        migrations.AddField(
            model_name='vorspeise',
            name='kundeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.kunde'),
        ),
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
