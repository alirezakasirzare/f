# Generated by Django 4.0.5 on 2022-06-13 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMainCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ProductMainCategoriesImage', verbose_name='Image')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999, verbose_name='Title')),
                ('dimensions', models.CharField(blank=True, max_length=999, null=True, verbose_name='Dimensions')),
                ('weight', models.CharField(blank=True, max_length=999, null=True, verbose_name='Weight')),
                ('slug', models.TextField()),
                ('main_image', models.ImageField(upload_to='productsImage', verbose_name='Image')),
                ('image1', models.ImageField(upload_to='productsImage', verbose_name='Image1')),
                ('image2', models.ImageField(upload_to='productsImage', verbose_name='Image2')),
                ('image3', models.ImageField(upload_to='productsImage', verbose_name='Image3')),
                ('image4', models.ImageField(upload_to='productsImage', verbose_name='Image4')),
                ('description', models.TextField(verbose_name='Description')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('discounted_price', models.IntegerField(blank=True, null=True, verbose_name='Discounted Price')),
                ('score', models.IntegerField(default=1, verbose_name='Score')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('inventory', models.IntegerField(verbose_name='Inventory')),
                ('status', models.BooleanField(blank=True, default=True, null=True, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsSliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ProductsSlides', verbose_name='Image')),
                ('url', models.URLField(verbose_name='Url')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubCategories_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubCategories_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='Name')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('sub_categories2', models.ManyToManyField(blank=True, to='products.productsubcategories_2', verbose_name='Sub Categories 2')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsTrackingCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_code', models.CharField(blank=True, max_length=150, null=True, verbose_name='Tracking Code')),
                ('code_status', models.BooleanField(blank=True, null=True, verbose_name='Code Status')),
                ('product_status', models.CharField(blank=True, choices=[('confirming', '???? ?????? ??????????'), ('confirmed', '?????????? ??????'), ('sending', '???? ?????? ??????????'), ('processed', '?????????? ???????? ????')], max_length=100, null=True, verbose_name='Product_status')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.carts', verbose_name='carts')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='"Total Score')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='Prodcut')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsComplaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='Prodcut Id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='colors',
            field=models.ManyToManyField(to='products.productscolors', verbose_name='Colors'),
        ),
        migrations.AddField(
            model_name='products',
            name='maincategories',
            field=models.ManyToManyField(to='products.productmaincategories', verbose_name='Main Category'),
        ),
        migrations.AddField(
            model_name='products',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sellers.sellers', verbose_name='Seller'),
        ),
        migrations.AddField(
            model_name='products',
            name='sizes',
            field=models.ManyToManyField(to='products.productssizes', verbose_name='Sizes'),
        ),
        migrations.AddField(
            model_name='products',
            name='subCategories1',
            field=models.ManyToManyField(to='products.productsubcategories_1', verbose_name='Sub Category 1'),
        ),
        migrations.AddField(
            model_name='products',
            name='subCategories2',
            field=models.ManyToManyField(to='products.productsubcategories_2', verbose_name='Sub Category 2'),
        ),
        migrations.AddField(
            model_name='productmaincategories',
            name='sub_categories1',
            field=models.ManyToManyField(blank=True, to='products.productsubcategories_1', verbose_name='Sub Categories 1'),
        ),
    ]
