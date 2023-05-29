# Generated by Django 4.1.5 on 2023-04-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_paid', models.FloatField()),
                ('salary_pending', models.FloatField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admn.teacher')),
            ],
        ),
    ]
