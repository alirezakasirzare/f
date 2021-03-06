# Generated by Django 4.0.5 on 2022-06-13 08:11

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
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=999, verbose_name='Business Name')),
                ('business_description', models.TextField(verbose_name='Business Description')),
                ('business_image', models.ImageField(upload_to='Businessimage', verbose_name='Business Image')),
                ('business_license', models.ImageField(upload_to='BusinessLicenseImage', verbose_name='Business License')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
                ('business_status', models.BooleanField(default=False, verbose_name='business Status')),
            ],
        ),
        migrations.CreateModel(
            name='SellersCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='SellersUsersMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sellers.sellers', verbose_name='Seller')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='SellersMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('file', models.FileField(blank=True, null=True, upload_to='SellersMessages', verbose_name='File')),
                ('is_seller', models.BooleanField(default=False, verbose_name='Is Seller')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sellers.sellers', verbose_name='Seller')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='sellers',
            name='business_categories',
            field=models.ManyToManyField(to='sellers.sellerscategories', verbose_name='business Categories'),
        ),
        migrations.AddField(
            model_name='sellers',
            name='business_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Business Owner'),
        ),
    ]
