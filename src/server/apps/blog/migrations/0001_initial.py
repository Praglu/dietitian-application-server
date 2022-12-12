# Generated by Django 4.1.3 on 2022-12-11 11:23

from django.db import migrations, models
import django.utils.timezone
import server.apps.blog.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('content_1', models.CharField(blank=True, max_length=512, null=True)),
                ('content_2', models.CharField(blank=True, max_length=512, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to=server.apps.blog.models.file_storage_path)),
                ('content_img', models.FileField(blank=True, null=True, upload_to=server.apps.blog.models.file_storage_path)),
            ],
        ),
    ]
