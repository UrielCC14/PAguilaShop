# Generated by Django 4.2.5 on 2023-10-15 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_zona_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
