# Generated by Django 4.1.3 on 2023-01-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='opinion_text',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='user_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
