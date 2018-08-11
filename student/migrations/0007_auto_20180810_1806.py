# Generated by Django 2.0.5 on 2018-08-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20180810_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.AddField(
            model_name='course',
            name='grade',
            field=models.CharField(choices=[('O', 'O'), ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('P', 'P'), ('F', 'F'), ('FE', 'FE'), ('', '')], default='', max_length=2),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]