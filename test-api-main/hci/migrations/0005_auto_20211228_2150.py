# Generated by Django 3.1.8 on 2021-12-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hci', '0004_auto_20211228_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instances',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]