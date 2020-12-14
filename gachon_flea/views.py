import json
import requests
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic import ListView, DetailView, TemplateView

from gachon_flea.forms import SearchForm
from gachon_flea.models import Product, Cart, ViewBuyList, ViewSellList, Comment, Review, BlackList, Profile
from mysite.views import OwnerOnlyMixin
from .tokens import account_activation_token


def exchangecurl(wallet, money):
    headers = {
        'Authorization': 'Bearer EPeknyLprhWaGvpmsWrvCQgdLbpXVsNyRM9EzCn53Dh5uH2AxSPMZFvcQtMDd1rH',
        'Content-Type': 'application/json'
    }

    body = {'inputs': {"receiverAddress": "0x1da6551a7d0ede0e9069b1a2321e4a90a948292e", 'valueAmount': '100000'}}

    response = requests.post('https://api.luniverse.io/tx/v1.1/transactions/Reward2', data=json.dumps(body),
                             headers=headers)

    print(response.content)


def chargecurl(wallet, money):
    headers = {
        'Authorization': 'Bearer EPeknyLprhWaGvpmsWrvCQgdLbpXVsNyRM9EzCn53Dh5uH2AxSPMZFvcQtMDd1rH',
        'Content-Type': 'application/json'
    }

    body = {'from': '0x1da6551a7d0ede0e9069b1a2321e4a90a948292e', 'inputs': {'valueAmount': '60000000000000000000'}}

    response = requests.post('https://api.luniverse.io/tx/v1.1/transactions/Support', data=json.dumps(body),
                             headers=headers)
    print(response.content)

def checkbal(wallet):

    headers = {
        'Authorization': 'Bearer EPeknyLprhWaGvpmsWrvCQgdLbpXVsNyRM9EzCn53Dh5uH2AxSPMZFvcQtMDd1rH',
        'Content-Type': 'application/json'
    }

    response = requests.get(
        'https://api.luniverse.io/tx/v1.0/wallets/0x1da6551a7d0ede0e9069b1a2321e4a90a948292e/FT9754/GT/balance',
        headers=headers)
    print("UserA wallet")
    print(response.content)
class MainLV(ListView): # 메인페이지
    model = Product
    template_name = 'gachon_flea/main.html'

class Mypage(LoginRequiredMixin, ListView): # 마이페이지
    model = Cart
    template_name = 'gachon_flea/Mypage.html'

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)

class SearchFormView(ListView): # 검색 결과 화면
    template_name = 'gachon_flea/Search.html'

class ProductCV(LoginRequiredMixin, CreateView): # 상품등록
    model = Product
    fields = ('name', 'price', 'img', 'description', 'category')
    success_url = reverse_lazy('gachon_flea:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDV(ListView): # 상품 id 기준으로 detial 화면
    model = Product
    template_name = 'gachon_flea/Product_detail.html'

class ProductBuy(ListView): # 상품 id 기준으로 구매하는 화면 (결제)
    template_name = 'gachon_flea/Product_buy.html'

class ProductReview(ListView): # 후기 등록화면
    template_name = 'gachon_flea/Product_Review.html'


# 카테고리
class FurnitureLV(ListView):
    model = Product
    template_name = 'gachon_flea/main/furniture.html'

class FoodLV(ListView):
    model = Product
    template_name = 'gachon_flea/main/food.html'

class SportsLV(ListView):
    model = Product
    template_name = 'gachon_flea/main/sports.html'

class ClothesLV(ListView):
    model = Product
    template_name = 'gachon_flea/main/clothes.html'

class HobbyLV(ListView):
    model = Product
    template_name = 'gachon_flea/main/hobby.html'

class BeautyLV(ListView):
    model = Product
    template_name = 'gachon_flea/main/beauty.html'

class BookLV(ListView):
    model = Product
    template_name = 'gachon_flea/main/book.html'

class EtcLV(ListView):
    model = Product
    template_name = 'gachon_flea/main/etc.html'

# 검색
class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'gachon_flea/Search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Product.objects.filter(Q(name__icontains=searchWord) |
                                           Q(description__icontains=searchWord)
                                           ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

#Mypage 들
class buy_ing(LoginRequiredMixin, ListView): #진행 중인 구매
    model = ViewBuyList
    template_name = 'gachon_flea/mypage/mypage_buy_ing.html'

class sell_ing(LoginRequiredMixin, ListView): # 진행 중인 판매
    model = ViewSellList
    template_name = 'gachon_flea/mypage/mypage_sell_ing.html'

    def get_queryset(self):
        return ViewSellList.objects.filter(owner=self.request.user)
    #def index(request):
     #   msg = 'My Message'
      #  return render(request, 'index.html', {'message': msg})

class got(LoginRequiredMixin, ListView): # 찜 목록
    model = Cart
    template_name = 'gachon_flea/mypage/mypage_got.html'

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)

class buy(LoginRequiredMixin, ListView): #구매 내역
    model = ViewBuyList
    template_name = 'gachon_flea/mypage/mypage_buy.html'

    def get_queryset(self):
        return ViewBuyList.objects.filter(owner=self.request.user)

class sell(LoginRequiredMixin, ListView): #판매 내역
    model = ViewSellList
    template_name = 'gachon_flea/mypage/mypage_sell.html'

    def get_queryset(self):
        return ViewSellList.objects.filter(owner=self.request.user)

class check_review(LoginRequiredMixin, ListView): # 후기 목록
    model = Review
    template_name = 'gachon_flea/mypage/mypage_check_review.html'

    def get_queryset(self):
        return Review.objects.filter(owner=self.request.user)





class confirm_buy(OwnerOnlyMixin, UpdateView):
    model = ViewBuyList
    template_name = 'confirm/confirm_buy.html'
    success_url = reverse_lazy('gachon_flea:mypage')


class cancel_cart(OwnerOnlyMixin, DeleteView):
    model = Cart
    template_name = 'confirm/cancel_cart.html'
    success_url = reverse_lazy('gachon_flea:mypage')


class make_review(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'confirm/make_review.html'
    success_url = reverse_lazy('gachon_flea:mypage')

class HomeView(TemplateView):
    template_name = 'home.html'

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


# 회원가입
def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        if str(email)[-15:] == 'gc.gachon.ac.kr':
            if request.POST["password1"] == request.POST["password2"]:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["email"],
                    last_name=request.POST["lastname"],
                    password=request.POST["password1"])
                user.is_active = False
                user.save()
                number = request.POST["number"]
                profile = Profile(user=user, number=number)



                profile.save()
                current_site = get_current_site(request)
                # localhost:8000
                message = render_to_string('gachon_flea/user_activate_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                    'token': account_activation_token.make_token(user),
                })
                mail_subject = "[SOT] 회원가입 인증 메일입니다."
                user_email = request.POST['email']
                email = EmailMessage(mail_subject, message, to=[user_email])
                email.send()

                return HttpResponse(
                    '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                    'justify-content: center; align-items: center;">'
                    '<span>입력하신 이메일로 인증 링크가 전송되었습니다.</span>'
                    '</div>'
                )
            else:
                messages.info(request, '비밀번호가 일치하지 않습니다.')

                return redirect('gachon_flea:signup')
        else:
            messages.info(request, '이메일 형식을 맞춰주세요')

            return redirect('gachon_flea:signup')


    return render(request, 'gachon_flea/signup.html')


# 로그인
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request, username=username, password=password)
        model = Profile(user=user)
        print(model.black)
        print(model.number)
        print(model.bad)
        print(model.good)

        print('-------------------------------------------------')
  #      if user is not None:
   #         if model.black == False:
    #            print('you')
     #           user.is_active = True
      #          return render(request, 'gachon_flea/login.html', {'error': 'username or password is incorrect'})

        if user is not None:
            auth.login(request, user)
            return redirect('gachon_flea:index')
        else:
            return render(request, 'gachon_flea/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'gachon_flea/login.html')

def logout(request):
    auth.logout(request)
    template_name = 'logout.html'
    return redirect('gachon_flea:index')

def activate(request, uid64, token):

    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True

        user.save()
        auth.login(request, user)
        return redirect('gachon_flea:index')
    else:
        return HttpResponse('비정상적인 접근입니다.')



#환전
def exchange(request):
    if request.method == "POST":
        money = request.POST['money']
        #wallet = self.request.user.wallet
        wallet = '0x1da6551a7d0ede0e9069b1a2321e4a90a948292e'
        exchangecurl(wallet, money)

        return render(request, 'gachon_flea/Mypage.html')
    return HttpResponse('비정상적인 접근입니다.')
#충전
def charge(request):
    if request.method == "POST":
        money = request.POST['money']
        #wallet = self.request.user.wallet
        wallet = '0x1da6551a7d0ede0e9069b1a2321e4a90a948292e'
    return HttpResponse('비정상적인 접근입니다.')
