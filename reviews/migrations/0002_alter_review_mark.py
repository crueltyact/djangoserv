# Generated by Django 4.1.5 on 2023-01-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.DecimalField(decimal_places=0, max_digits=2, max_length=10, verbose_name='Rate us'),
        ),
    ]