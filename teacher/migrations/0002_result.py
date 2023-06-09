# Generated by Django 4.1.5 on 2023-03-30 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FileField(upload_to='results/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admn.teacher')),
            ],
        ),
    ]
