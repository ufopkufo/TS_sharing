from django.db import models
from activities.models import activity
from personalInfo.models import User
from datetime import datetime
class Post(models.Model):
    # 动态内容
    content = models.TextField()
    # 发布动态时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 作者
    writer= models.ForeignKey(User, on_delete=models.CASCADE, related_name='square_writer',default='')
    # 浏览量
    views = models.PositiveIntegerField(default=0)
    # 话题名称#
    activity = models.ForeignKey(activity, on_delete=models.CASCADE, related_name='square_post_activity', default='')
    #点赞
    users_like = models.ManyToManyField(User, related_name="post_like", blank=True)
    def __str__(self):
        return self.content


class comment(models.Model):
    #回复用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户',related_name='square_post_user_comment')
    #回复动态名称
    post = models.ForeignKey(Post, verbose_name='动态', on_delete=models.CASCADE,related_name='square_post_comment')
    #评论内容
    comments = models.TextField(verbose_name='评论')
    #添加时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = '帖子评论'
        verbose_name_plural = verbose_name
        ordering = ('-add_time',)