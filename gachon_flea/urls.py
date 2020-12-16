from django.urls import path
from gachon_flea import views
from django.conf.urls import url

app_name = 'gachon_flea'
urlpatterns = [
    path('', views.MainLV.as_view(), name='index'),  # 메인페이지

    path('mypage/', views.buy_ing.as_view(), name='mypage'),  # 마이페이지

    path('search/', views.SearchFormView.as_view(), name='search'),  # 검색 결과 화면

    path('add/', views.ProductCV.as_view(), name="add"),  # 상품등록

    path('detail/<int:pk>/<slug>', views.PostDV.as_view(), name='detail'),  # 상품 id 기준으로 detail 화면
   
    path('buy/<int:pk>', views.ProductBuy.as_view(), name="update"),  # 상품 id 기준으로 구매하는 화면 (결제)

    # 카테고리
    path('furniture/', views.FurnitureLV.as_view(), name='furniture'),
    path('food/', views.FoodLV.as_view(), name='food'),
    path('sports/', views.SportsLV.as_view(), name='sports'),
    path('clothes/', views.ClothesLV.as_view(), name='clothes'),
    path('hobby/', views.HobbyLV.as_view(), name='hobby'),
    path('beauty/', views.BeautyLV.as_view(), name='beauty'),
    path('book/', views.BookLV.as_view(), name='book'),
    path('etc/', views.EtcLV.as_view(), name='etc'),

    path('mypage/buy_ing/', views.buy_ing.as_view(), name='buy_ing'),
    path('mypage/sell_ing/', views.sell_ing.as_view(), name='sell_ing'),
    path('mypage/got/', views.got.as_view(), name='got'),
    path('mypage/review/', views.check_review.as_view(), name='check_review'),
    path('mypage/wallet/', views.mywallet.as_view(), name='wallet'),

    path('mypage/review/', views.check_review.as_view(), name='check_review'),
    path('mypage/review/create/', views.create_review.as_view(), name='create_review'),
    path('mypage/review/<int:pk>/modify/', views.modify_review.as_view(), name='modify_review'),
    path('mypage/review/<int:pk>/delete/', views.delete_review.as_view(), name='delete_review'),


    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name="activate"),

    path('confirm/buy/<int:pk>', views.confirm_buy, name='confirm_buy'),
    path('cancel/got/<int:pk>', views.cancel_cart.as_view(), name='cancel_got'),
    path('confirm/make_review/<int:pk>', views.make_review.as_view(), name='make_review'),

    path('charge/', views.charge, name='charge'),
    path('exchange/', views.exchange, name='exchange'),
    
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='detail'),
    
        url(r'^$', views.product_list, name='product_list'),
    path('detail/add/<int:id>/', views.product_detail, name='add_cart'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),



]
