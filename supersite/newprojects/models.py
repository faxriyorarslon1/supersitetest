from django.db import models


OPERATINGBUSINESS = [
        ('YES', 'Yes'),
        ('NO', 'No')
    ]

BUSINESS_TYPE = [
        ('STARTUP', 'Startup'),
        ('FRANCHISE', 'Franchise'),
        ('READYBUSINESS', 'Ready Business')
]

class NewProjects(models.Model):
    image = models.ImageField(upload_to='new_projects/')
    title = models.CharField(max_length=30)
    description = models.CharField(max_length = 200)
    suminvest = models.IntegerField()
    operatingbusiness = models.CharField(max_length=3,choices=OPERATINGBUSINESS)
    numberworker = models.IntegerField()
    status = models.CharField(max_length=30)
    businesstype = models.CharField(max_length=15, choices=BUSINESS_TYPE)

    class Meta:
        verbose_name = "Yangi Loyiha"
        verbose_name_plural = 'Yangi Loyihalar'
