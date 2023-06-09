# Generated by Django 4.1.7 on 2023-06-12 05:37

import businesses.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=businesses.utils.bs_category_file_name)),
                ('marker', models.ImageField(blank=True, null=True, upload_to=businesses.utils.markers_file_name)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Business Categories',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='BusinessCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('address', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=businesses.utils.business_file_name)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('customer_service_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('slug', models.SlugField()),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('address', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=businesses.utils.business_branch_file_name)),
                ('is_approved', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='businesses.businesscatalog')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='businesses.businesscategory')),
            ],
        ),
    ]
