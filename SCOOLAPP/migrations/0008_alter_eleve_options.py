# Generated by Django 4.1.4 on 2023-01-02 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SCOOLAPP', '0007_eleve'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eleve',
            options={'ordering': ['nomElev']},
        ),
    ]