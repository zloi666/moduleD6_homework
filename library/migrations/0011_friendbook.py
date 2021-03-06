# Generated by Django 3.2 on 2021-06-25 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in', models.DateTimeField()),
                ('date_out', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('friend_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.friend')),
            ],
        ),
    ]
