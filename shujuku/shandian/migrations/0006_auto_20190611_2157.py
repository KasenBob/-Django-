# Generated by Django 2.2.2 on 2019-06-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shandian', '0005_sales_records_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_records',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]