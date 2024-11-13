from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_view, name='index'),  # 초기 화면 URL (홈페이지)
    path('supply/', views.supply_view, name='supply'), # 매물 등록 페이지
    path('supply/my_list/', views.my_list_view, name='my_list'),  # 내 매물 페이지
    path('supply/listing/<int:id>/', views.listing_detail_view, name='listing_detail'),  # 매물 상세 페이지
    path('supply/accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('supply/listing/<int:id>/update/', views.listing_update_view, name='listing_update'), # 수정/삭제
    path('supply/listing/<int:id>/delete/', views.listing_delete_view, name='listing_delete'),
     # 새로운 페이지: 다른 사용자가 등록한 모든 매물 보기
    path('supply/all_listings/', views.all_listings_view, name='all_listings'),
    path('supply/my_listings_only/', views.my_listings_only_view, name='my_listings_only'),  # 내 매물 목록만 보기
   


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
