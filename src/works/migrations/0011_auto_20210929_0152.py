# Generated by Django 3.2.6 on 2021-09-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0010_alter_word_phrase'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalstage',
            name='digest',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='hash'),
        ),
        migrations.AddField(
            model_name='stage',
            name='digest',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='hash'),
        ),
    ]
