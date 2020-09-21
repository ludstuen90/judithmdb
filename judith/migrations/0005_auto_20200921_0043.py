# Generated by Django 3.1 on 2020-09-21 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judith', '0004_auto_20200920_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolioitem',
            options={'ordering': ['priority']},
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='priority',
            field=models.IntegerField(default=999, help_text='El ítem con el número más grande va a aparecer primero en el portafolio'),
            preserve_default=False,
        ),
    ]