# Generated by Django 4.2.6 on 2023-11-13 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_newsletters_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenementcampagne',
            name='type_evenement',
            field=models.CharField(max_length=50),
        ),
    ]