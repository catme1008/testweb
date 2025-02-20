from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()



"""
create table app01_userinfo()
id bigint auto_increment primary key
name varchar(32),
password varchar(64),
age int
"""
class Robots(models.Model):
    name = models.CharField(max_length=16)
    type = models.CharField(max_length=16)
    reg_time = models.CharField(max_length=16)
    service_time=models.CharField(max_length=16,null=True,blank=True)

# Robots.objects.create(name='robot1')
# insert into app01_Robot
