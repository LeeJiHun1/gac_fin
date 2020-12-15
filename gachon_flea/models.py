from django.db import models
from django.contrib.auth.models import User
from gachon_flea.fields import ThumbnailImageField
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('영문', max_length=20)
    K_name = models.CharField('한글', max_length=20)

    def __str__(self):
        return self.K_name

class Product(models.Model):
    name = models.CharField('이름', max_length = 20) # 상품명
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null=True)
    price = models.CharField('가격', max_length = 20,) # 상품 가격
    date = models.DateField('게시글 올린 날짜', auto_now_add=True) # 게시글 올린 날짜
    img = ThumbnailImageField('이미지', upload_to='gachon_flea/%Y/%m')
    description = models.TextField('상품 설명')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('gachon_flea:detail', args=(self.id,))

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE, blank= True, null=True)
    class Meta:
        ordering = ('owner',)

    def get_absolute_url(self):
        return reverse('gachon_flea:detail', args=(self.product_id,))
class ViewBuyList(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE, blank = True, null = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null=True)
    before = models.BooleanField('판매 여부', default = False) # F = 구매 전 T = 구매 후


    class Meta:
        ordering = ('owner',)
    def get_absolute_url(self):
        return reverse('gachon_flea:detail', args=(self.product_id,))

class ViewSellList(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE, blank = True, null = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null=True)
    before = models.BooleanField('판매 여부', default = False) # F = 판매 전 T = 판매 후
    class Meta:
        ordering = ('owner',)
    def get_absolute_url(self):
        return reverse('gachon_flea:detail', args=(self.product_id,))

class Comment(models.Model):
    date = models.DateTimeField('CREATE DATE', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete =models.CASCADE, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField("COMMENT", null=True)
    class Meta:
        ordering = ('owner',)

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    evaluation = models.BooleanField('EVALUATION')
    content = models.TextField('CONTENTS', blank=True)


    class Meta:
        ordering = ('owner',)


class BlackList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ('user_id',)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField('학번', max_length=20)
    wallet = models.CharField('Wallet',max_length=50, blank = True, null = True)
    good = models.IntegerField('좋아요',default=0)
    bad = models.IntegerField('싫어요',default=0)
    record_bad = models.IntegerField('초기화싫어요',default=0)
    black = models.BooleanField('블랙리스트', default=False)