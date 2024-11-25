# Generated by Django 5.1.2 on 2024-10-25 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_visitor_aadhar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='home.inmate')),
            ],
        ),
    ]
