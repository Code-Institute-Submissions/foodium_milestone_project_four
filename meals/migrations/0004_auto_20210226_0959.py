# Generated by Django 3.1.5 on 2021-02-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_auto_20210204_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='people',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='preparation_time',
            field=models.IntegerField(blank=True),
        ),
    ]