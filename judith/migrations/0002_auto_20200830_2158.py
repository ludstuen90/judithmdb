# Generated by Django 3.1 on 2020-08-30 21:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('judith', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepageitems',
            name='linked_in_url',
        ),
        migrations.RemoveField(
            model_name='homepageitems',
            name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='homepageitems',
            name='youtube_url',
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='instagram_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='linked_in_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='telegram_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='twitter_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='youtube_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]