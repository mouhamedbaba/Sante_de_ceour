# Generated by Django 4.2.6 on 2023-11-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_workspace_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspacecolumn',
            name='background',
        ),
        migrations.AddField(
            model_name='workspace',
            name='background',
            field=models.ImageField(null=True, upload_to='task/workspace/background/'),
        ),
    ]
