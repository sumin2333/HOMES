from django import forms
from .models import PropertyListing

class PropertyListingForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = ['면적','가격','관리비', '건물연식', '층수', '방', '욕실', 
    '주차공간여부', '주변환경' , '기타사항'
 ]
        widgets = {
            'house_type': forms.Select(attrs={'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
        }