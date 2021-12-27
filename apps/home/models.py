from django.db import models


# Create your models here.
class GarbageSort(models.Model):
    name = models.CharField(verbose_name="分类名称", max_length=30)
    explain = models.TextField(verbose_name="分类说明", blank=True)
    require = models.TextField(verbose_name="投放指导", blank=True)
    common = models.TextField(verbose_name="常见垃圾", blank=True)


class Garbage(models.Model):
    name = models.CharField(verbose_name="垃圾名字", max_length=30)
    sort = models.ForeignKey(GarbageSort, related_name="name", verbose_name="分类名称", on_delete=models.SET_NULL,
                             blank=True, null=True)


class RecoveryRecord(models.Model):
    STATUS_CHOICES = (
        ("guest", "待收取"),
        ("member", "待确认"),
        ("volunteer", "已确认"),
        ("director", "已完成"),
        ("administrator", "已取消")
    )
    code = models.CharField(verbose_name="验证码", blank=True)
    status = models.CharField(verbose_name="订单状态", choices=)

