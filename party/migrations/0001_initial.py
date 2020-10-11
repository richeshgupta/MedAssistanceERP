# Generated by Django 3.1 on 2020-10-11 16:41

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party_Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('contact', phone_field.models.PhoneField(blank=True, help_text='Company_Number', max_length=31)),
                ('doctor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Party_Wholeseller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('gstin', models.IntegerField()),
                ('dl_number', models.PositiveIntegerField()),
                ('contact', phone_field.models.PhoneField(blank=True, help_text='Company_Number', max_length=31)),
                ('pan_number', models.CharField(max_length=11, unique=True)),
            ],
        ),
    ]
