# Generated by Django 3.0.6 on 2020-06-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourguide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PLACE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('logitude', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
