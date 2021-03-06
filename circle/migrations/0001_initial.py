# Generated by Django 3.0.7 on 2020-06-12 07:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('classification', models.CharField(choices=[('0', '无'), ('1', '置顶'), ('2', '精华'), ('3', '精华且置顶')], default='', max_length=50, verbose_name='身份标识')),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='circle_post', to='circle.circle')),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(verbose_name='评论')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='circle.Post', verbose_name='帖子')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '帖子评论',
                'verbose_name_plural': '帖子评论',
                'ordering': ('-add_time',),
            },
        ),
    ]
