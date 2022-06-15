# Generated by Django 4.0.5 on 2022-06-13 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Payment Date')),
                ('payment_status', models.BooleanField(default=False, verbose_name='Payment Status')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=999, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price')),
                ('count', models.IntegerField(blank=True, default=1, null=True, verbose_name='Count')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')),
                ('payment_status', models.BooleanField(default=False, verbose_name='Payment Status')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.carts', verbose_name='Cart')),
            ],
        ),
    ]
