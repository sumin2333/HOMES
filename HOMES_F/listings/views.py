
from django.shortcuts import render, redirect, get_object_or_404
from .models import PropertyListing,  PropertyImage
from django.contrib import messages
from .forms import PropertyListingForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import default_storage


def index_view(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'supply.html')

def property_register(request):
    if request.method == 'POST':
        house_type = request.POST.get('house_type')
        transaction_type = request.POST.get('transaction_type')
        
        property_listing = PropertyListing.objects.create(
            house_type=house_type,
            transaction_type=transaction_type,
        )
        
        return redirect('listing_detail', pk=property_listing.pk)

    return render(request, 'supply.html')

def listing_detail(request, pk):
    listing = get_object_or_404(PropertyListing, pk=pk)
    return render(request, 'listing_detail.html', {'listing': listing})

@login_required
def supply_view(request):
    if request.method == 'POST':
        form = PropertyListingForm(request.POST, request.FILES)
        if form.is_valid():
            # 로그인한 사용자의 정보로 매물 등록
            property_listing = form.save(commit=False)
            property_listing.user = request.user  # 로그인한 사용자 설정
            property_listing.save()
            messages.success(request, '매물이 성공적으로 등록되었습니다.')
            return redirect('my_list')  # 등록 후 메인 페이지로 이동
    else:
        form = PropertyListingForm()
    return render(request, 'listings/supply.html', {'form': form})

#내 매물 페이지 뷰 
def my_list_view(request):
    listings = None
    if request.method == "POST":
        # 로그인한 사용자만 자신의 매물을 볼 수 있도록 필터링
        listings = PropertyListing.objects.filter(user=request.user)
        
    
    return render(request, 'listings/my_list.html', {'listings': listings})

#내 매물 목록 페이지 
def my_listings_only_view(request):
    # 현재 로그인한 사용자의 매물만 필터링하여 가져옵니다.
    listings = PropertyListing.objects.filter(user=request.user)
    return render(request, 'my_list_only.html', {'listings': listings})

def listing_list_view(request):
    listings = PropertyListing.objects.filter(user=request.user)  # 로그인한 사용자만 필터링
    return render(request, 'listings/my_list.html', {'listings': listings})

# 매물 상세 페이지 뷰
def listing_detail_view(request, id):
    listing = get_object_or_404(PropertyListing, id=id)

  # 이전 매물과 다음 매물 찾기
    previous_listing = PropertyListing.objects.filter(id__lt=listing.id).order_by('-id').first()
    next_listing = PropertyListing.objects.filter(id__gt=listing.id).order_by('id').first()

    images = listing.images.all()
    

    if request.method == 'POST' :
        image_count = 0

        # 7개의 이미지를 각각 처리
        for i in range(1, 8):
            image_field = f'image{i}'
            image = request.FILES.get(image_field)
            if images:
                PropertyImage.objects.create(property_listing=listing, image=image)
                image_count += 1
     
                messages.success(request, '이미지가 성공적으로 업로드되었습니다.')  
        if image_count > 0:
            return redirect('listing_detail', id=listing.id)
        
    
    return render(request, 'listings/listing_detail.html', {
        'listing': listing,
        'images': images,
        'previous_listing': previous_listing,
        'next_listing': next_listing,
        'error_message': "최대 7장까지만 업로드 가능합니다."
            })

# 매물 수정 뷰 함수
def listing_update_view(request, id):
    listing = get_object_or_404(PropertyListing, id=id)

    if request.method == 'POST':
        form = PropertyListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', id=listing.id)
        else:
            # form이 유효하지 않을 경우, 오류를 디버그하기 위해 출력
            print(form.errors)
    else:
        form = PropertyListingForm(instance=listing)

    return render(request, 'listings/listing_update.html', {'form': form, 'listing': listing})

# 매물 삭제 뷰 함수
def listing_delete_view(request, id):
    listing = get_object_or_404(PropertyListing, id=id)

    if request.method == 'POST':
        listing.delete()
        return redirect('my_list')

    return render(request, 'listings/listing_confirm_delete.html', {'listing': listing})

# 모든 매물 보기 뷰
def all_listings_view(request):
  
    listings = PropertyListing.objects.all()
    return render(request, 'listings/all_listings.html', {'listings': listings})
    
def supply_add(request):
    if request.method == 'POST':
        house_type = request.POST.get('house_type')
        transaction_type = request.POST.get('transaction_type')
        print(house_type, transaction_type)
        return render(request, 'listings/my_list.html')