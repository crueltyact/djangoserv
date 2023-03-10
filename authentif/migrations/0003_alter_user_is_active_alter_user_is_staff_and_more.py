# Generated by Django 4.1.5 on 2023-01-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentif', '0002_user_groups_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='activated'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='admin'),
        ),
    ]
