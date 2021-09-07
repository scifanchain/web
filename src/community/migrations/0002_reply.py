# Generated by Django 3.2.6 on 2021-09-06 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='内容')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '删除'), (1, '正常'), (2, '冻结')], default=1, verbose_name='状态')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.topic', verbose_name='评论主题')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]