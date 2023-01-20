# Generated by Django 4.1.5 on 2023-01-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Template name')),
                ('desc', models.TextField(max_length=255, verbose_name='Description')),
                ('cover', models.ImageField(upload_to='users/photos', verbose_name='Cover')),
            ],
            options={
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
            },
        ),
    ]