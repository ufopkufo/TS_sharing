from django.db import models
from personalInfo.models import User
from activities.models import activity
from datetime import datetime

class circle(models.Model):
    #圈子名称#
    name = models.CharField(max_length=30, unique=True)
    #圈子描述#
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    #帖子名称#
    title = models.CharField(max_length=100, verbose_name='标题')
    #最新回复时间
    last_updated = models.DateTimeField(auto_now=True)
    #发帖时间
    create_time = models.DateTimeField(default=datetime.now)
    #所属圈子
    circle = models.ForeignKey(circle,on_delete=models.CASCADE, related_name='circle_post')
    #发帖人
    starter= models.ForeignKey(User,on_delete=models.CASCADE, related_name='circle_starter_post')
    #帖子内容
    content = models.TextField()
    #浏览量
    views = models.PositiveIntegerField(default=0)
    #是否为精华、置顶
    classification=models.CharField(choices=(('0', '无'), ('1', '置顶'), ('2', '精华'),('3','精华且置顶')),
                                    max_length=50, default='0', verbose_name='帖子标示')
    #话题名称#
    activity = models.ForeignKey(activity,on_delete=models.CASCADE, related_name='circle_post',default='')
    def __str__(self):
        return self.title
class comment(models.Model):
    #回复用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户',related_name='circle_post_user_comment')
    #回复帖子名称
    post = models.ForeignKey(Post, verbose_name='帖子', on_delete=models.CASCADE,related_name='circle_post_comment')
    #评论内容
    comments = models.TextField(verbose_name='评论')
    #添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = '帖子评论'
        verbose_name_plural = verbose_name
        ordering = ('-add_time',)