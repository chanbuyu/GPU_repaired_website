# Generated by Django 3.2.7 on 2022-04-23 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='the_id',
            field=models.CharField(max_length=32, null=True, unique=True, verbose_name='订单编号'),
        ),
    ]
