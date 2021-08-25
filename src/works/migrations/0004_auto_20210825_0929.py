# Generated by Django 3.2.6 on 2021-08-25 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_auto_20210825_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstage',
            name='belong_to_chapter',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='works.chapter', verbose_name='所属章节'),
        ),
        migrations.AlterField(
            model_name='historicalstage',
            name='belong_to_story',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='works.story', verbose_name='所属故事'),
        ),
        migrations.AlterField(
            model_name='historicalstage',
            name='pv',
            field=models.PositiveIntegerField(default=1, verbose_name='浏览量'),
        ),
        migrations.AlterField(
            model_name='historicalstage',
            name='uv',
            field=models.PositiveIntegerField(default=1, verbose_name='访问人数'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='belong_to_chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.chapter', verbose_name='所属章节'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='belong_to_story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.story', verbose_name='所属故事'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='pv',
            field=models.PositiveIntegerField(default=1, verbose_name='浏览量'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='uv',
            field=models.PositiveIntegerField(default=1, verbose_name='访问人数'),
        ),
    ]