# Generated by Django 3.1.8 on 2021-12-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('currentStep', models.IntegerField(default=0)),
                ('totalStep', models.IntegerField(default=0)),
                ('steps', models.IntegerField(default=0)),
                ('stepReports', models.IntegerField(default=0)),
                ('totalErrorCount', models.IntegerField(default=0)),
                ('serviceUnits', models.IntegerField(default=0)),
                ('executionInstanceId', models.CharField(max_length=100)),
                ('instanceMetrics', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
