# Generated by Django 2.1.4 on 2019-02-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sin', '0008_auto_20190228_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
