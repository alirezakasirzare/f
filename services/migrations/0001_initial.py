# Generated by Django 4.0.4 on 2022-05-22 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999, verbose_name='Title service')),
                ('image', models.ImageField(upload_to='services', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
                ('short_description', models.TextField(verbose_name='Description')),
                ('score', models.IntegerField(default=1, verbose_name='Score')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesCompanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
                ('management', models.CharField(max_length=999, verbose_name='Management')),
                ('established_year', models.CharField(max_length=999, verbose_name='Established Year')),
                ('address', models.CharField(max_length=999, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesSliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ServicesSliders', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='Score')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services', verbose_name='Service Id')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('payment_status', models.BooleanField(default=False, verbose_name='Payment status')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services', verbose_name='Service Id')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Status')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services', verbose_name='Service Id')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesCollaborationHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(blank=True, max_length=999, null=True, verbose_name='Hours')),
                ('service_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_reservation', to='services.services', verbose_name='Service User')),
            ],
        ),
        migrations.AddField(
            model_name='services',
            name='categories',
            field=models.ManyToManyField(to='services.servicescategories', verbose_name='Categories'),
        ),
        migrations.AddField(
            model_name='services',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicescompanies', verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='services',
            name='service_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='service user'),
        ),
    ]
