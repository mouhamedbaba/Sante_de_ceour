# Generated by Django 4.2.6 on 2023-10-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_alter_collect_image_alter_collect_raised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='raised',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
    ]