# Generated by Django 3.0.4 on 2020-04-21 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_plan', '0003_externalresource'),
    ]

    operations = [
        migrations.RenameField(
            model_name='externalresource',
            old_name='ClientPresentation',
            new_name='clientPresentation',
        ),
    ]
