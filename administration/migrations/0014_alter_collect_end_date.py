# Generated by Django 4.2.6 on 2023-10-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0013_alter_collect_post_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
