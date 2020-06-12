from django.db import models
from personalInfo.models import User
class activity(models.Model):
    #活动名称#
    name = models.CharField(max_length=30, unique=True)
    #活动描述#
    description = models.CharField(max_length=200)
    #发起人
    starter = models.ForeignKey(User,on_delete=models.CASCADE, related_name='activitystarter_post',default='')
    def __str__(self):
        return self.name