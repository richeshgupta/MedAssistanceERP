# Generated by Django 3.1 on 2020-10-14 19:46

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('party', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_email', models.EmailField(max_length=254)),
                ('mode_of_payment', models.PositiveSmallIntegerField(choices=[(1, 'Cash'), (2, 'Credit')], default=1)),
                ('total_bill', models.FloatField()),
                ('name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=35), size=None)),
                ('company', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('batch_number', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('quantity', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('discount', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), size=None)),
                ('deal', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=None)),
                ('tax', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), size=None)),
                ('loss', django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(default=False), size=None)),
                ('sale_rate', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(null=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('mode_of_payment', models.PositiveSmallIntegerField(choices=[(1, 'Cash'), (2, 'Credit')], default=1)),
                ('total_bill', models.FloatField()),
                ('name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=35), size=None)),
                ('company', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('batch_number', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('quantity', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('discount', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), size=None)),
                ('deal', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=None)),
                ('tax', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), size=None)),
                ('purchase_rate', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(null=True), size=None)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='party.party_wholeseller')),
            ],
        ),
    ]
