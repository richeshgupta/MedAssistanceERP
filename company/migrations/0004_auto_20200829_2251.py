# Generated by Django 3.1 on 2020-08-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20200829_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='comp_GST',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_of_packing',
            field=models.PositiveIntegerField(),
        ),
    ]
