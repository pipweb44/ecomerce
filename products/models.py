from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الفئة")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="الوصف")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="صورة الفئة")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            import uuid
            base_slug = slugify(self.name)
            if not base_slug:
                base_slug = str(uuid.uuid4())[:8]
            self.slug = base_slug

            # التأكد من أن slug فريد
            counter = 1
            original_slug = self.slug
            while Category.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:category_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="الفئة")
    description = models.TextField(verbose_name="الوصف")
    short_description = models.CharField(max_length=300, blank=True, verbose_name="وصف مختصر")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="سعر الخصم")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="الكمية المتوفرة")
    image = models.ImageField(upload_to='products/', verbose_name="الصورة الرئيسية")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    is_featured = models.BooleanField(default=False, verbose_name="منتج مميز")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            import uuid
            base_slug = slugify(self.name)
            if not base_slug:
                base_slug = str(uuid.uuid4())[:8]
            self.slug = base_slug

            # التأكد من أن slug فريد
            counter = 1
            original_slug = self.slug
            while Product.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})

    @property
    def get_price(self):
        """إرجاع السعر النهائي (مع الخصم إن وجد)"""
        if self.discount_price:
            return self.discount_price
        return self.price

    @property
    def has_discount(self):
        """التحقق من وجود خصم"""
        return self.discount_price is not None and self.discount_price < self.price

    @property
    def discount_percentage(self):
        """حساب نسبة الخصم"""
        if self.has_discount:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    @property
    def is_in_stock(self):
        """التحقق من توفر المنتج"""
        return self.stock_quantity > 0


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="المنتج")
    image = models.ImageField(upload_to='products/gallery/', verbose_name="الصورة")
    alt_text = models.CharField(max_length=200, blank=True, verbose_name="النص البديل")
    is_main = models.BooleanField(default=False, verbose_name="صورة رئيسية")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "صورة المنتج"
        verbose_name_plural = "صور المنتجات"
        ordering = ['-is_main', 'created_at']

    def __str__(self):
        return f"صورة {self.product.name}"
