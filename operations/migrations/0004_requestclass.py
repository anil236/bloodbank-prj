# Generated by Django 4.1 on 2022-10-31 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_rename_donate_donater_delete_stockinput'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_request', models.CharField(max_length=100)),
                ('last_name_request', models.CharField(max_length=100)),
                ('birthday_request', models.IntegerField()),
                ('email_request', models.EmailField(max_length=100)),
                ('ph_no_request', models.BigIntegerField()),
                ('address_request', models.CharField(max_length=200)),
                ('bloodgroup_request', models.CharField(max_length=10)),
            ],
        ),
    ]
