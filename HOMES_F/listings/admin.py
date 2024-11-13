from django.contrib import admin
from .models import PropertyListing, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
class PropertyListingAdmin(admin.ModelAdmin):
    list_display = ['주소', '기타사항', '가격', '면적', '층수', '방', '욕실', '주차공간여부', '건물연식', '관리비', 'images']
    inlines = [PropertyImageInline]
    
admin.site.register(PropertyListing)
admin.site.register(PropertyImage) 