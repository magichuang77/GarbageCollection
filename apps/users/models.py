from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    """
    用户信息
    """
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    ROLE_CHOICES = (
        ("guest", "游客"),
        ("member", "会员"),
        ("volunteer", "志愿者"),
        ("director", "负责人"),
        ("administrator", "管理员"),
    )

    # 用户用邮箱注册，姓名、生日和邮箱可以为空
    nick_name = models.CharField("姓名", default='神秘人士', max_length=30)
    gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
    role = models.CharField("角色", max_length=13, choices=ROLE_CHOICES, default="member")
    email = models.EmailField("邮箱", max_length=100, default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    desc = models.CharField(max_length=50, verbose_name='个性签名', default='人生苦短，我用Python')
    image = models.ImageField(upload_to='users/%Y/%m', default='image/default.png', blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
