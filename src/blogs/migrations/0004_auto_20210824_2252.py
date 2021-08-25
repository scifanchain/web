# Generated by Django 3.2.6 on 2021-08-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210824_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_time',
            new_name='created',
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
    ]