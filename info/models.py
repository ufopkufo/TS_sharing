from django.db import models
from personalInfo.models import User
from datetime import datetime
class message(models.Model):
    #两名用户
    user1=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user1',verbose_name='用户1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2', verbose_name='用户2')
    #聊天内容
    content= models.TextField()
    #发送时间
    send_time=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.content
class notify (models.Model):
    #通知
    starter=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notify_starter',verbose_name='通知发起者')
    #指定收到学生的学院
    academy = models.CharField(max_length=50, default='', verbose_name='学院')
    #指定收到学生的年级
    pgrade = models.CharField(max_length=50, default='', verbose_name='年级')
    #通知内容
    content = models.TextField()
    # 发送时间
    send_time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.content
class announcement(models.Model):
    starter=models.ForeignKey(User,on_delete=models.CASCADE,related_name='announcement_starter',verbose_name='公告发起者')
    #公告内容
    content = models.TextField()
    # 发送时间
    send_time = models.DateTimeField(default=datetime.now)