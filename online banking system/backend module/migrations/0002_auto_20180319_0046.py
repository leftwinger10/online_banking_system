# Generated by Django 2.0.2 on 2018-03-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_account',
            name='amount',
            field=models.IntegerField(max_length=20),
        ),
    ]