# Generated by Django 4.1 on 2022-10-30 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0002_donater_bloodgroup_alter_donater_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='donater',
        ),
    ]