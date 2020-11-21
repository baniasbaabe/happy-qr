# Generated by Django 3.1.2 on 2020-11-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0002_auto_20201114_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.CharField(choices=[('Standard', 'Standard'), ('Deluxe', 'Deluxe'), ('Modern', 'Modern')], default='Standard', max_length=20)),
            ],
        ),
    ]
