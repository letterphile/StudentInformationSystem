# Generated by Django 2.0.5 on 2018-08-10 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20180810_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='attendance',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='internal',
            field=models.PositiveIntegerField(null=True),
        ),
    ]