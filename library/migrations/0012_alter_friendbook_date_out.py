# Generated by Django 3.2 on 2021-06-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_friendbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendbook',
            name='date_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
