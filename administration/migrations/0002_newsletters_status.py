# Generated by Django 4.2.6 on 2023-11-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletters',
            name='status',
            field=models.CharField(default='abonne', max_length=50),
        ),
    ]