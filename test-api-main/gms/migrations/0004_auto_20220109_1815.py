# Generated by Django 3.1.8 on 2022-01-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gms', '0003_auto_20220108_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integertable',
            name='Access_KEY',
            field=models.CharField(default='AKIASP6I3H4VJMQDGZHG', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='integertable',
            name='Acess_Secret_key',
            field=models.CharField(default='uOwZp0GyHWFTrdZhnbb/6HZcrorwNnRKn6TDZfR3', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='integertable',
            name='END_POINT',
            field=models.CharField(default='https://elasticbeanstalk-us-east-2-171683036970.s3.us-east-2.amazonaws.com/', max_length=100, null=True),
        ),
    ]
