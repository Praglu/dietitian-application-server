# Generated by Django 4.1.3 on 2022-12-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentblock', '0003_rename_blog_aboutcontentblock_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcontentblock',
            name='button_text',
            field=models.IntegerField(choices=[(None, '(unknown)'), (0, 'Check offer'), (1, 'Find out more')], default='(unknown)'),
        ),
        migrations.AlterField(
            model_name='homecontentblock',
            name='button_text',
            field=models.IntegerField(choices=[(None, '(unknown)'), (0, 'Check offer'), (1, 'Find out more')], default='(unknown)'),
        ),
    ]
