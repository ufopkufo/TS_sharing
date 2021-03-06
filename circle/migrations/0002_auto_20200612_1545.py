# Generated by Django 3.0.7 on 2020-06-12 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
        ('circle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='activity',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='circle_post', to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='post',
            name='classification',
            field=models.CharField(choices=[('0', '无'), ('1', '置顶'), ('2', '精华'), ('3', '精华且置顶')], default='0', max_length=50, verbose_name='帖子标示'),
        ),
    ]
