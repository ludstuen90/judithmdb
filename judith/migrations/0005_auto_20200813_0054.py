# Generated by Django 3.1 on 2020-08-13 00:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('judith', '0004_auto_20200813_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='fecha_de_publicacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
