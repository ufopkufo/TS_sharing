from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    #姓名
    pname = models.CharField(max_length=50, blank=True)
    #头像
    avatar = models.ImageField(null=True, upload_to='User/%Y%m%d', blank=True)
    #出生年月
    date_of_birth = models.DateField(blank=True, null=True)
    #学院
    pacademy=models.CharField(max_length=50, default='', verbose_name='学院')
    #年级
    pgrade=models.CharField(max_length=50, default='', verbose_name='年级')
    #兴趣
    phobby=models.CharField(max_length=50, default='', verbose_name='个人兴趣')
    #身份标示
    pidentity = models.CharField(choices=(('0', '学生'), ('1', '学校组织'), ('2', '老师'), ('3', '管理员')),max_length=50, default='', verbose_name='身份标识')
    #个人标签
    ptag = models.TextField('个人标签', null=True, blank=True)


    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = "用户"


class Follows(models.Model):
    """关注表"""
    follow = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow',verbose_name='被关注的，作者')
    fan = models.ForeignKey(User,on_delete=models.CASCADE,related_name='fan',verbose_name='粉丝')

    def __str__(self):
        return str(self.follow.id)

    class Meta:
        ordering = ('-follow',)
