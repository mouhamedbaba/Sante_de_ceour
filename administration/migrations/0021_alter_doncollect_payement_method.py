# Generated by Django 4.2.6 on 2023-11-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0020_evenementcampagne_oraganisateurs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doncollect',
            name='payement_method',
            field=models.CharField(blank=True, default='wave', max_length=50),
        ),
    ]
