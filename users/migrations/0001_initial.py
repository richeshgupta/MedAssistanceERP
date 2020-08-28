# Generated by Django 3.1 on 2020-08-28 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.IntegerField(choices=[(1, 'basic'), (2, 'Intermediate'), (3, 'Admin')], default=1)),
                ('address', models.CharField(default='', max_length=100)),
                ('mobile', phone_field.models.PhoneField(blank=True, help_text='Mobile_Number', max_length=31)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]