# Generated by Django 2.1.4 on 2019-02-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sin', '0004_category_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]