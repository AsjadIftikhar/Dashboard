# Generated by Django 3.1.8 on 2022-01-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hci', '0011_auto_20211231_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='dueDate',
            field=models.DateField(auto_now=True),
        ),
    ]
