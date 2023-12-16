from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    quantity = models.CharField(max_length=20, verbose_name='剩余数量')
    qq = models.CharField(max_length=20, verbose_name='qq号')
    security = models.CharField(max_length=20, verbose_name='密保')
    creation_date = models.DateField()
    recent_login = models.DateField()

    class Meta:
        db_table = 'user'

class IP1(models.Model):
    ip = models.CharField(max_length=20, verbose_name='ip')
    post = models.CharField(max_length=20, verbose_name='端口')

    class Meta:
        db_table = 'IP1'
class CarMy(models.Model):
    quota = models.CharField(max_length=20, verbose_name='额度')
    token = models.CharField(max_length=50, verbose_name='卡密')

    class Meta:
        db_table = 'carmy'


