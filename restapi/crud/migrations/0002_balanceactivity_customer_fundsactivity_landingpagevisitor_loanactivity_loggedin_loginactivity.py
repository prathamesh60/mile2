# Generated by Django 2.1.15 on 2020-06-10 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=20)),
                ('account_type', models.CharField(max_length=20)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='FundsActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
        migrations.CreateModel(
            name='LandingPageVisitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
        migrations.CreateModel(
            name='LoanActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
        migrations.CreateModel(
            name='LoggedIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
        migrations.CreateModel(
            name='LoginActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('visit_date', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('visit_time', models.TimeField(blank=True, verbose_name='Conversation Time')),
            ],
        ),
    ]
