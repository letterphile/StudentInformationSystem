# Generated by Django 2.0.5 on 2018-08-11 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0024_auto_20180811_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=45)),
                ('course_code', models.CharField(max_length=7)),
                ('grade', models.CharField(choices=[('O', 'O'), ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('P', 'P'), ('F', 'F'), ('FE', 'FE'), ('', '')], default='', max_length=2)),
                ('attendance', models.PositiveIntegerField(null=True)),
                ('internal', models.PositiveIntegerField(null=True)),
                ('branch', models.ManyToManyField(to='student.Branch')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.CurrentSemester')),
            ],
            options={
                'ordering': ('course_code',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('roll_no', models.PositiveIntegerField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Batch')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Branch')),
                ('course', models.ManyToManyField(to='student.Course')),
                ('current_semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.CurrentSemester')),
                ('past_semester', models.ManyToManyField(to='student.PastSemester')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
