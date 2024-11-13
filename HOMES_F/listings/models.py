from django.db import models
from django.contrib.auth.models import User

class PropertyListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # user와 매물 연결
    
    HOUSE_TYPE_CHOICES = [
        ('villa', '빌라/주택'),
        ('officetel', '오피스텔'),
        ('apartment', '아파트'),
        ('commercial', '상가/사무실'),
    ]

    TRANSACTION_TYPE_CHOICES = [
        ('monthly_rent', '월세'),
        ('jeonse', '전세'),
        ('sale', '매매'),
    ]

    house_type = models.CharField(
        max_length=20,
        choices=HOUSE_TYPE_CHOICES,
        default='villa'
    )
    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPE_CHOICES,
        default='sale'
    )
    주소 = models.CharField(max_length=255, blank=True)
    면적 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    층수  = models.PositiveIntegerField(default=0)
    가격 = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    방 = models.IntegerField(default=0)
    욕실 = models.IntegerField(default=0)
    주차공간여부 = models.PositiveIntegerField(default=0)
    건물연식 = models.PositiveIntegerField(default=0)
    관리비 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    주변환경 = models.TextField(blank=True)
    기타사항 = models.TextField(blank=True)

def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property_listing = models.ForeignKey('PropertyListing', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

def __str__(self):
        return f"Image for {self.property_listing.title}"

