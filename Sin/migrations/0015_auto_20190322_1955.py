# Generated by Django 2.1.4 on 2019-03-22 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sin', '0014_bill_created_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
