# Generated by Django 4.0.4 on 2022-05-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('team_image', models.ImageField(upload_to='static_cdn/media_root/TeamImage')),
            ],
        ),
    ]
