# Generated by Django 3.2.6 on 2021-09-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0009_auto_20210912_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='phrase',
            field=models.TextField(),
        ),
    ]
