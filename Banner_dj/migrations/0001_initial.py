# Generated by Django 3.2 on 2022-08-05 20:53

import Banner_dj.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('float', models.BooleanField(default=True)),
                ('align_vertical', models.CharField(choices=[('right', 'Right'), ('center', 'Center'), ('left', 'Left')], max_length=15)),
                ('align_horizontal', models.CharField(choices=[('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom')], max_length=15)),
                ('width', models.CharField(default='auto', max_length=10)),
                ('height', models.CharField(default='auto', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(help_text='Enter the address of the page where you want the banner to be displayed - (without domain address)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Banner_dj.models.upload_image_banner)),
                ('image_url', models.URLField(blank=True, help_text='You can set image url instead image', null=True)),
                ('href', models.URLField(help_text='When it is clicked , it will be redirect to this address')),
                ('count_click', models.IntegerField(default=0)),
                ('pages', models.ManyToManyField(to='Banner_dj.Page')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Banner_dj.bannerstyle')),
            ],
        ),
    ]
