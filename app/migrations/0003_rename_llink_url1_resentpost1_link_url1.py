# Generated by Django 4.2.13 on 2024-11-17 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_about_foodgallery_foodgallerymain_post2list_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resentpost1',
            old_name='llink_url1',
            new_name='link_url1',
        ),
    ]