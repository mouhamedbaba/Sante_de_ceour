# Generated by Django 4.2.6 on 2023-11-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationPayTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_event', models.CharField(max_length=20)),
                ('client_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=20, null=True)),
                ('item_name', models.CharField(max_length=255)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ref_command', models.CharField(max_length=255)),
                ('command_name', models.CharField(max_length=255)),
                ('currency', models.CharField(blank=True, max_length=3, null=True)),
                ('env', models.CharField(max_length=10)),
                ('custom_field', models.TextField(blank=True, null=True)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
    ]
