# Generated by Django 3.2 on 2021-07-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='covers'),
        ),
    ]
