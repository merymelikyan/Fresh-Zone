# Generated by Django 4.2.13 on 2024-11-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_webdesine_webdesign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('image_title', models.CharField(max_length=255)),
                ('image_class', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='gallery')),
                ('link_url', models.CharField(max_length=255)),
                ('link_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Gallery1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('image_title', models.CharField(max_length=255)),
                ('image_class', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='gallery')),
                ('link_url1', models.URLField(max_length=255)),
                ('link_name1', models.CharField(max_length=255)),
                ('link_url2', models.URLField(max_length=255)),
                ('link_name2', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Gallery1',
                'verbose_name_plural': 'Gallery1',
            },
        ),
        migrations.CreateModel(
            name='GalleryMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Gallery Main',
                'verbose_name_plural': 'Gallery Main',
            },
        ),
        migrations.AlterModelOptions(
            name='webdesign',
            options={'verbose_name': 'Web Design', 'verbose_name_plural': 'Web Design'},
        ),
    ]