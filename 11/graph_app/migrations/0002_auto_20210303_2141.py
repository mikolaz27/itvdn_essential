# Generated by Django 3.1.7 on 2021-03-03 19:41

from django.db import migrations
import graph_app.managers


class Migration(migrations.Migration):

    dependencies = [
        ('graph_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='apiclient',
            managers=[
                ('objects', graph_app.managers.UserManager()),
            ],
        ),
    ]