# Generated by Django 3.1 on 2020-09-20 19:25

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('judith', '0003_auto_20200911_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='biocastellano',
            name='bio_below_the_fold_text',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioingles',
            name='bio_below_the_fold_text',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now, help_text='Agregue la segunda mitad del bio acá (que en mobile, aparece cuando hagan clic en leer más'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bioingles',
            name='bio_text',
            field=ckeditor.fields.RichTextField(help_text='Agregue la primera mitad del bio acá'),
        ),
    ]