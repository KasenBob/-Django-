# Generated by Django 2.2.2 on 2019-06-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shandian', '0004_auto_20190611_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_records',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
    ]
