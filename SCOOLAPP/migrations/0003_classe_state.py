# Generated by Django 4.1.4 on 2022-12-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCOOLAPP', '0002_classe_descrpclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
