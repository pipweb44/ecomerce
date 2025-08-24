# 👨‍💻 دليل المطورين - Developer Guide

## 📋 فهرس المحتويات

1. [إعداد بيئة التطوير](#إعداد-بيئة-التطوير)
2. [هيكل الكود](#هيكل-الكود)
3. [معايير البرمجة](#معايير-البرمجة)
4. [الاختبارات](#الاختبارات)
5. [إضافة مميزات جديدة](#إضافة-مميزات-جديدة)
6. [استكشاف الأخطاء](#استكشاف-الأخطاء)
7. [أدوات التطوير](#أدوات-التطوير)

---

## 🛠️ إعداد بيئة التطوير

### المتطلبات الأساسية
```bash
Python 3.8+
Git
VS Code أو PyCharm (مُوصى به)
```

### خطوات الإعداد
```bash
# 1. استنساخ المشروع
git clone <repository-url>
cd ecommerce

# 2. إنشاء البيئة الافتراضية
python -m venv venv

# 3. تفعيل البيئة الافتراضية
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. تثبيت المتطلبات
pip install -r requirements.txt
pip install -r requirements-dev.txt  # أدوات التطوير

# 5. إعداد قاعدة البيانات
python manage.py makemigrations
python manage.py migrate

# 6. إنشاء بيانات تجريبية
python manage.py loaddata fixtures/sample_data.json

# 7. إنشاء مستخدم إداري
python manage.py createsuperuser

# 8. تشغيل الخادم
python manage.py runserver
```

### إعدادات VS Code
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=88"],
    "editor.formatOnSave": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        "**/venv": true,
        "**/node_modules": true
    }
}
```

---

## 🏗️ هيكل الكود

### تنظيم التطبيقات
```
ecommerce/
├── core/           # إعدادات المشروع الأساسية
├── accounts/       # إدارة المستخدمين والمصادقة
├── products/       # إدارة المنتجات والفئات
├── orders/         # إدارة الطلبات والسلة
├── customers/      # إدارة بيانات العملاء
└── utils/          # أدوات مساعدة مشتركة
```

### هيكل التطبيق الواحد
```
app_name/
├── __init__.py
├── admin.py        # إعدادات لوحة الإدارة
├── apps.py         # تكوين التطبيق
├── models.py       # نماذج قاعدة البيانات
├── views.py        # منطق العرض
├── urls.py         # توجيه URLs
├── forms.py        # نماذج Django
├── serializers.py  # مسلسلات API (إذا لزم الأمر)
├── tests/          # اختبارات التطبيق
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_views.py
│   └── test_forms.py
├── migrations/     # ملفات الهجرة
└── management/     # أوامر إدارية مخصصة
    └── commands/
```

### أنماط التسمية
```python
# Models - PascalCase
class Product(models.Model):
    pass

# Views - snake_case
def product_list_view(request):
    pass

# URLs - kebab-case
path('product-list/', views.product_list_view, name='product_list')

# Templates - kebab-case
# templates/products/product-list.html

# CSS Classes - kebab-case
.product-card { }

# JavaScript Functions - camelCase
function addToCart() { }
```

---

## 📏 معايير البرمجة

### Python Code Style (PEP 8)
```python
# استيراد المكتبات
import os
import sys
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from .utils import helper_function

# الثوابت
MAX_PRODUCT_NAME_LENGTH = 200
DEFAULT_CATEGORY_SLUG = 'uncategorized'

# النماذج
class Product(models.Model):
    """نموذج المنتج مع جميع المعلومات المطلوبة."""
    
    name = models.CharField(
        max_length=MAX_PRODUCT_NAME_LENGTH,
        verbose_name='اسم المنتج',
        help_text='أدخل اسم المنتج (حد أقصى 200 حرف)'
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """إرجاع رابط المنتج."""
        return reverse('products:detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'
        ordering = ['-created_at']

# الدوال
def calculate_total_price(items):
    """حساب السعر الإجمالي لقائمة من العناصر."""
    total = 0
    for item in items:
        total += item.price * item.quantity
    return total
```

### JavaScript Code Style
```javascript
// استخدام const/let بدلاً من var
const API_BASE_URL = '/api/v1/';
let cartItems = [];

// الدوال
function addToCart(productId, quantity = 1) {
    // التحقق من صحة المدخلات
    if (!productId || quantity < 1) {
        throw new Error('معاملات غير صحيحة');
    }
    
    // منطق الدالة
    const item = {
        productId: productId,
        quantity: quantity,
        addedAt: new Date()
    };
    
    cartItems.push(item);
    updateCartDisplay();
}

// استخدام async/await
async function fetchProducts() {
    try {
        const response = await fetch(`${API_BASE_URL}products/`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('خطأ في جلب المنتجات:', error);
        throw error;
    }
}

// Event Listeners
document.addEventListener('DOMContentLoaded', function() {
    initializeCart();
    setupEventListeners();
});
```

### CSS/SCSS Code Style
```scss
// المتغيرات
$primary-color: #1e3a8a;
$secondary-color: #3b82f6;
$border-radius: 8px;
$transition-speed: 0.3s;

// Mixins
@mixin button-style($bg-color, $text-color: white) {
    background-color: $bg-color;
    color: $text-color;
    border: none;
    border-radius: $border-radius;
    padding: 12px 24px;
    transition: all $transition-speed ease;
    
    &:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba($bg-color, 0.3);
    }
}

// الفئات
.product-card {
    background: var(--dark-card);
    border-radius: $border-radius;
    padding: 1.5rem;
    transition: transform $transition-speed ease;
    
    &:hover {
        transform: translateY(-4px);
    }
    
    &__image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: $border-radius;
    }
    
    &__title {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 1rem 0 0.5rem;
    }
    
    &__price {
        font-size: 1.5rem;
        font-weight: 700;
        color: $primary-color;
    }
}

.btn {
    &--primary {
        @include button-style($primary-color);
    }
    
    &--secondary {
        @include button-style($secondary-color);
    }
}
```

---

## 🧪 الاختبارات

### إعداد الاختبارات
```python
# tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product

class ProductModelTest(TestCase):
    def setUp(self):
        """إعداد البيانات للاختبار."""
        self.category = Category.objects.create(
            name='إلكترونيات',
            slug='electronics'
        )
        
        self.product = Product.objects.create(
            name='هاتف ذكي',
            slug='smartphone',
            price=999.99,
            category=self.category,
            stock_quantity=10
        )
    
    def test_product_creation(self):
        """اختبار إنشاء منتج جديد."""
        self.assertEqual(self.product.name, 'هاتف ذكي')
        self.assertEqual(self.product.category, self.category)
        self.assertTrue(self.product.is_active)
    
    def test_product_str_method(self):
        """اختبار دالة __str__ للمنتج."""
        self.assertEqual(str(self.product), 'هاتف ذكي')
    
    def test_product_absolute_url(self):
        """اختبار رابط المنتج."""
        expected_url = f'/product/{self.product.slug}/'
        self.assertEqual(self.product.get_absolute_url(), expected_url)
```

### اختبارات Views
```python
# tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Category

class ProductViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='إلكترونيات',
            slug='electronics'
        )
        
        self.product = Product.objects.create(
            name='هاتف ذكي',
            slug='smartphone',
            price=999.99,
            category=self.category
        )
    
    def test_product_list_view(self):
        """اختبار صفحة قائمة المنتجات."""
        url = reverse('products:product_list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'هاتف ذكي')
        self.assertContains(response, '999.99')
    
    def test_product_detail_view(self):
        """اختبار صفحة تفاصيل المنتج."""
        url = reverse('products:product_detail', kwargs={'slug': self.product.slug})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
```

### تشغيل الاختبارات
```bash
# تشغيل جميع الاختبارات
python manage.py test

# تشغيل اختبارات تطبيق محدد
python manage.py test products

# تشغيل اختبار محدد
python manage.py test products.tests.test_models.ProductModelTest.test_product_creation

# تشغيل مع تقرير التغطية
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## ➕ إضافة مميزات جديدة

### 1. إضافة نموذج جديد
```python
# في models.py
class Review(models.Model):
    """نموذج تقييمات المنتجات."""
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='المنتج'
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='المستخدم'
    )
    
    rating = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name='التقييم'
    )
    
    comment = models.TextField(
        max_length=500,
        verbose_name='التعليق'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإنشاء'
    )
    
    class Meta:
        verbose_name = 'تقييم'
        verbose_name_plural = 'التقييمات'
        unique_together = ['product', 'user']
    
    def __str__(self):
        return f'{self.user.username} - {self.product.name} ({self.rating}/5)'
```

### 2. إضافة View جديد
```python
# في views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@login_required
def add_review(request, product_slug):
    """إضافة تقييم للمنتج."""
    product = get_object_or_404(Product, slug=product_slug)
    
    # التحقق من عدم وجود تقييم سابق
    if Review.objects.filter(product=product, user=request.user).exists():
        messages.error(request, 'لقد قمت بتقييم هذا المنتج مسبقاً')
        return redirect('products:detail', slug=product_slug)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if rating and comment:
            Review.objects.create(
                product=product,
                user=request.user,
                rating=int(rating),
                comment=comment
            )
            messages.success(request, 'تم إضافة تقييمك بنجاح')
        else:
            messages.error(request, 'يرجى ملء جميع الحقول')
    
    return redirect('products:detail', slug=product_slug)
```

### 3. إضافة URL جديد
```python
# في urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # URLs موجودة...
    path('product/<slug:product_slug>/review/', views.add_review, name='add_review'),
]
```

### 4. إضافة Template
```html
<!-- templates/products/review_form.html -->
<div class="review-form mt-4">
    <h5>إضافة تقييم</h5>
    {% if user.is_authenticated %}
        <form method="post" action="{% url 'products:add_review' product.slug %}">
            {% csrf_token %}
            
            <div class="mb-3">
                <label class="form-label">التقييم</label>
                <div class="rating">
                    {% for i in "12345" %}
                        <input type="radio" name="rating" value="{{ i }}" id="star{{ i }}" required>
                        <label for="star{{ i }}">⭐</label>
                    {% endfor %}
                </div>
            </div>
            
            <div class="mb-3">
                <label for="comment" class="form-label">التعليق</label>
                <textarea class="form-control" id="comment" name="comment" rows="3" required></textarea>
            </div>
            
            <button type="submit" class="btn btn-primary">إضافة التقييم</button>
        </form>
    {% else %}
        <p><a href="{% url 'accounts:login' %}">سجل دخولك</a> لإضافة تقييم</p>
    {% endif %}
</div>
```

---

## 🐛 استكشاف الأخطاء

### أخطاء شائعة وحلولها

#### 1. خطأ Migration
```bash
# المشكلة: تعارض في migrations
django.db.migrations.exceptions.InconsistentMigrationHistory

# الحل:
python manage.py migrate --fake-initial
# أو
python manage.py migrate app_name zero
python manage.py migrate app_name
```

#### 2. خطأ Static Files
```bash
# المشكلة: الملفات الثابتة لا تظهر
# الحل:
python manage.py collectstatic
# تأكد من إعدادات STATIC_URL و STATIC_ROOT
```

#### 3. خطأ Template
```python
# المشكلة: TemplateDoesNotExist
# الحل: تأكد من مسار Template في TEMPLATES setting
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # تأكد من هذا المسار
        'APP_DIRS': True,
        # ...
    },
]
```

### أدوات التشخيص
```python
# في views.py - إضافة logging
import logging
logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug(f'Request data: {request.POST}')
    try:
        # كود الـ view
        pass
    except Exception as e:
        logger.error(f'Error in my_view: {str(e)}')
        raise

# في settings.py - إعداد logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'your_app_name': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

---

## 🔧 أدوات التطوير

### أدوات مفيدة
```bash
# Django Debug Toolbar
pip install django-debug-toolbar

# Django Extensions (shell_plus, runserver_plus)
pip install django-extensions

# Code formatting
pip install black isort

# Linting
pip install flake8 pylint

# Testing
pip install pytest-django coverage
```

### إعداد pre-commit hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
```

### أوامر مفيدة
```bash
# تنسيق الكود
black .
isort .

# فحص الكود
flake8 .
pylint your_app/

# إنشاء migration
python manage.py makemigrations app_name

# عرض SQL للـ migration
python manage.py sqlmigrate app_name 0001

# فحص المشروع
python manage.py check

# shell محسن
python manage.py shell_plus

# إنشاء بيانات وهمية
python manage.py shell_plus --notebook
```

---

## 📚 مصادر إضافية

### وثائق Django
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)

### أدوات مفيدة
- [Django Packages](https://djangopackages.org/)
- [Awesome Django](https://github.com/wsvincent/awesome-django)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

**آخر تحديث:** ديسمبر 2024
