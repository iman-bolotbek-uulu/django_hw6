# Generated by Django 3.2 on 2022-12-09 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=11)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
                ('position', models.CharField(max_length=30, verbose_name='Position')),
                ('salary', models.IntegerField(verbose_name='Salary')),
                ('work_experience', models.DateField(verbose_name='Work experience')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='VIPClient',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.client')),
                ('vip_status_start', models.DateField(auto_now=True, verbose_name='VIP start')),
                ('donation_amount', models.IntegerField(verbose_name='Amount donated by client')),
            ],
            options={
                'abstract': False,
            },
            bases=('employee.client',),
        ),
        migrations.CreateModel(
            name='WorkProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30, verbose_name='Project name')),
                ('members', models.ManyToManyField(related_name='projects', through='employee.Membership', to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=16)),
                ('id_card', models.CharField(max_length=12)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passports', to='employee.employee')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.workproject'),
        ),
    ]
