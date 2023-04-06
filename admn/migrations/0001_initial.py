# Generated by Django 4.1.5 on 2023-03-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('mobile', models.BigIntegerField()),
                ('email', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('salary', models.FloatField()),
                ('image', models.ImageField(upload_to='teacher_images/')),
                ('clas', models.BigIntegerField()),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]