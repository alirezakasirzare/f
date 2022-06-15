# Generated by Django 3.0 on 2022-04-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('company_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=99)),
                ('message', models.TextField()),
                ('status', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]