# Generated by Django 3.1 on 2020-10-14 19:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=20, verbose_name='Company Name')),
                ('comp_address', models.CharField(max_length=50, verbose_name='Company Address')),
                ('comp_gst', models.PositiveIntegerField(verbose_name='GST Number')),
                ('contact', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('scheduled_drug', models.BooleanField(default=False)),
                ('unit_of_packing', models.CharField(max_length=15)),
                ('sale_rate', models.FloatField(null=True)),
                ('gst', models.FloatField(null=True)),
                ('free', models.IntegerField(null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_number', models.CharField(max_length=10, verbose_name='Batch Number')),
                ('expiry', models.DateField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField()),
                ('mrp', models.FloatField(verbose_name='MRP')),
                ('purchase_rate', models.FloatField(null=True)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='company.product')),
            ],
        ),
    ]
