# Generated by Django 4.2.7 on 2023-11-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='units',
            field=models.CharField(max_length=200, null=True),
        ),
    ]