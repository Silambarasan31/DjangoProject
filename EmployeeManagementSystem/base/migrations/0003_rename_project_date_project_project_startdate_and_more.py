# Generated by Django 5.0.1 on 2024-02-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_project_project_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_date',
            new_name='project_startdate',
        ),
        migrations.AddField(
            model_name='project',
            name='project_enddate',
            field=models.DateField(null=True),
        ),
    ]
