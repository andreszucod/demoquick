# Generated by Django 3.1.4 on 2022-06-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220625_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.IntegerField(blank=True, null=True, verbose_name='Documento'),
        ),
    ]
