# Generated by Django 4.1.7 on 2023-06-12 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('businesses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='businesses.businessbranch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write_business', models.BooleanField(default=False)),
                ('write_branch', models.BooleanField(default=False)),
                ('write_product', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='management.businessstaff')),
            ],
        ),
    ]