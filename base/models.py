from tabnanny import verbose
from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Customer(models.Model):
    name = models.CharField(verbose_name="客户姓名", max_length=200, null=True)
    telephone = models.CharField(verbose_name="电话", max_length=200, null=True)
    address = models.CharField(verbose_name="收货地址", max_length=200, null=True)

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}--{self.telephone}'


class Order(models.Model):
    STATUS = (('正在清洗中..','已接单'), 
              ('已清洗，正在修复中..','已清洗'), 
              ('已修复，正在检测中..', '已维修'), 
              ('各项检测正常，已发回', '已完成'))

    date = models.DateTimeField(verbose_name="收卡时间", auto_now=True)
    brand = models.CharField(verbose_name="品牌", max_length=100, null=True)
    name = models.CharField(verbose_name="型号", max_length=100, null=True)
    status = models.CharField(verbose_name="订单状态", max_length=20, choices=STATUS, default='have order')
    sn_pic = ProcessedImageField(verbose_name="SN码照片", blank=True, null=True,
                                    upload_to='SN/',
                                    format='JPEG',
                                    options={'quality': 20}
                                    )
    before_pic_front = ProcessedImageField(verbose_name="维修前图片正面", blank=True, null=True,
                                    upload_to='order/',
                                    format='JPEG',
                                    options={'quality': 20}
                                    )
    before_pic_back = ProcessedImageField(verbose_name="维修前图片反面", blank=True, null=True,
                                    upload_to='order/',
                                    format='JPEG',
                                    options={'quality': 20}
                                    )                                
    repaired_pic_front = ProcessedImageField(verbose_name="维修后图片正面", blank=True, null=True,
                                    upload_to='repaired/',
                                    format='JPEG',
                                    options={'quality': 20}
                                    )
    repaired_pic_back = ProcessedImageField(verbose_name="维修后图片反面", blank=True, null=True,
                                    upload_to='repaired/',
                                    format='JPEG',
                                    options={'quality': 20}
                                    )                                
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        verbose_name = '显卡订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.date.strftime("%Y-%m-%d %H:%M")}--{self.brand}{self.name}'