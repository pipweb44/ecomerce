# 📚 وثائق متجري الإلكتروني - Complete Documentation

## 📋 فهرس المحتويات

1. [نظرة عامة](#نظرة-عامة)
2. [البنية التقنية](#البنية-التقنية)
3. [التثبيت والإعداد](#التثبيت-والإعداد)
4. [هيكل المشروع](#هيكل-المشروع)
5. [قاعدة البيانات](#قاعدة-البيانات)
6. [نظام المصادقة](#نظام-المصادقة)
7. [إدارة المنتجات](#إدارة-المنتجات)
8. [نظام الطلبات](#نظام-الطلبات)
9. [واجهة المستخدم](#واجهة-المستخدم)
10. [الأمان والحماية](#الأمان-والحماية)
11. [الأداء والتحسين](#الأداء-والتحسين)
12. [API Endpoints](#api-endpoints)

---

## 🎯 نظرة عامة

### وصف المشروع
متجري الإلكتروني هو منصة تجارة إلكترونية شاملة مطورة باستخدام Django Framework. يوفر النظام تجربة تسوق متكاملة للعملاء مع لوحة إدارة متطورة للمديرين.

### الأهداف الرئيسية
- **تجربة مستخدم ممتازة**: واجهة سهلة الاستخدام ومتجاوبة
- **إدارة فعالة**: أدوات إدارية شاملة للمنتجات والطلبات
- **أمان عالي**: حماية البيانات والمعاملات
- **قابلية التوسع**: بنية قابلة للتطوير والتحسين

### المستخدمون المستهدفون
- **العملاء**: المتسوقون الذين يبحثون عن منتجات
- **المديرون**: أصحاب المتاجر ومديرو المحتوى
- **المطورون**: فريق التطوير والصيانة

---

## 🏗️ البنية التقنية

### التقنيات الأساسية
```
Backend Framework: Django 5.2.5
Database: SQLite (Production: PostgreSQL)
Frontend: Bootstrap 5.3 + Custom CSS
Admin Panel: Django Jazzmin
Authentication: Django Auth System
File Handling: Pillow
```

### معمارية النظام
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (Templates)   │◄──►│   (Django)      │◄──►│   (SQLite)      │
│   Bootstrap     │    │   Views/Models  │    │   Models        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### متطلبات النظام
- **Python**: 3.8 أو أحدث
- **Django**: 5.2.5
- **Memory**: 512MB RAM (الحد الأدنى)
- **Storage**: 1GB مساحة فارغة
- **Browser**: متصفح حديث يدعم HTML5/CSS3

---

## 🚀 التثبيت والإعداد

### 1. إعداد البيئة
```bash
# إنشاء مجلد المشروع
mkdir ecommerce-project
cd ecommerce-project

# إنشاء البيئة الافتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 2. تثبيت المتطلبات
```bash
# تثبيت Django والمكتبات المطلوبة
pip install Django==5.2.5
pip install django-jazzmin==3.0.1
pip install Pillow==11.3.0

# أو تثبيت من ملف المتطلبات
pip install -r requirements.txt
```

### 3. إعداد قاعدة البيانات
```bash
# إنشاء migrations
python manage.py makemigrations

# تطبيق migrations
python manage.py migrate

# إنشاء مستخدم إداري
python manage.py createsuperuser
```

### 4. تشغيل الخادم
```bash
# تشغيل خادم التطوير
python manage.py runserver

# الوصول للموقع
# الموقع الرئيسي: http://127.0.0.1:8000
# لوحة الإدارة: http://127.0.0.1:8000/admin
```

---

## 📁 هيكل المشروع

### الهيكل العام
```
ecomerce/
├── 📁 core/                    # إعدادات Django الرئيسية
│   ├── settings.py            # إعدادات المشروع
│   ├── urls.py                # URLs الرئيسية
│   ├── wsgi.py                # إعدادات WSGI
│   └── asgi.py                # إعدادات ASGI
├── 📁 accounts/               # نظام المصادقة
│   ├── models.py              # نماذج المستخدمين
│   ├── views.py               # views المصادقة
│   ├── urls.py                # URLs المصادقة
│   └── forms.py               # نماذج المصادقة
├── 📁 products/               # إدارة المنتجات
│   ├── models.py              # نماذج المنتجات
│   ├── views.py               # views المنتجات
│   ├── urls.py                # URLs المنتجات
│   └── admin.py               # إعدادات الإدارة
├── 📁 orders/                 # نظام الطلبات
│   ├── models.py              # نماذج الطلبات
│   ├── views.py               # views الطلبات
│   ├── urls.py                # URLs الطلبات
│   └── cart.py                # منطق السلة
├── 📁 customers/              # إدارة العملاء
│   ├── models.py              # نماذج العملاء
│   ├── views.py               # views العملاء
│   └── admin.py               # إعدادات الإدارة
├── 📁 templates/              # قوالب HTML
│   ├── base.html              # القالب الأساسي
│   ├── 📁 products/           # قوالب المنتجات
│   ├── 📁 orders/             # قوالب الطلبات
│   └── 📁 accounts/           # قوالب المصادقة
├── 📁 static/                 # الملفات الثابتة
│   ├── 📁 css/                # ملفات CSS
│   ├── 📁 js/                 # ملفات JavaScript
│   └── 📁 images/             # الصور الثابتة
├── 📁 media/                  # ملفات المستخدمين
│   └── 📁 products/           # صور المنتجات
├── manage.py                  # أداة إدارة Django
├── requirements.txt           # متطلبات المشروع
└── README.md                  # وثائق المشروع
```

### وصف التطبيقات

#### Core App
- **الغرض**: إعدادات Django الأساسية
- **المحتوى**: settings, URLs, WSGI/ASGI
- **الأهمية**: نقطة البداية لكامل المشروع

#### Accounts App
- **الغرض**: إدارة المستخدمين والمصادقة
- **المميزات**: تسجيل دخول، تسجيل، ملف شخصي
- **الأمان**: حماية كلمات المرور، جلسات آمنة

#### Products App
- **الغرض**: إدارة المنتجات والفئات
- **المميزات**: عرض، بحث، فلترة المنتجات
- **الوسائط**: رفع وإدارة صور المنتجات

#### Orders App
- **الغرض**: إدارة الطلبات والسلة
- **المميزات**: سلة تسوق، إتمام طلبات، تتبع
- **التفاعل**: AJAX للتحديث الفوري

#### Customers App
- **الغرض**: إدارة بيانات العملاء
- **المميزات**: ملفات العملاء، عناوين، تفضيلات
- **الربط**: مرتبط بنظام المصادقة

---

## 🗄️ قاعدة البيانات

### نماذج البيانات الرئيسية

#### 1. نموذج المستخدم (User)
```python
# Django's built-in User model
- id: Primary Key
- username: اسم المستخدم (فريد)
- email: البريد الإلكتروني
- first_name: الاسم الأول
- last_name: اسم العائلة
- password: كلمة المرور (مشفرة)
- is_active: حالة النشاط
- date_joined: تاريخ التسجيل
```

#### 2. نموذج العميل (Customer)
```python
class Customer:
    - id: UUID (Primary Key)
    - user: OneToOne → User
    - phone: رقم الهاتف
    - address: العنوان
    - city: المدينة
    - postal_code: الرمز البريدي
    - birth_date: تاريخ الميلاد
    - created_at: تاريخ الإنشاء
    - updated_at: تاريخ التحديث
```

#### 3. نموذج الفئة (Category)
```python
class Category:
    - id: UUID (Primary Key)
    - name: اسم الفئة
    - slug: الرابط المختصر
    - description: الوصف
    - image: صورة الفئة
    - is_active: حالة النشاط
    - created_at: تاريخ الإنشاء
    - updated_at: تاريخ التحديث
```

#### 4. نموذج المنتج (Product)
```python
class Product:
    - id: UUID (Primary Key)
    - name: اسم المنتج
    - slug: الرابط المختصر
    - description: الوصف
    - price: السعر
    - category: ForeignKey → Category
    - image: الصورة الرئيسية
    - stock_quantity: الكمية المتوفرة
    - is_active: حالة النشاط
    - is_featured: منتج مميز
    - created_at: تاريخ الإنشاء
    - updated_at: تاريخ التحديث
```

#### 5. نموذج صور المنتج (ProductImage)
```python
class ProductImage:
    - id: UUID (Primary Key)
    - product: ForeignKey → Product
    - image: الصورة
    - alt_text: النص البديل
    - is_primary: صورة رئيسية
    - created_at: تاريخ الإنشاء
```

#### 6. نموذج الطلب (Order)
```python
class Order:
    - id: UUID (Primary Key)
    - order_number: رقم الطلب (فريد)
    - user: ForeignKey → User
    - customer_name: اسم العميل
    - customer_email: بريد العميل
    - customer_phone: هاتف العميل
    - shipping_address: عنوان التسليم
    - shipping_city: مدينة التسليم
    - shipping_postal_code: الرمز البريدي
    - status: حالة الطلب
    - total_amount: المبلغ الإجمالي
    - shipping_cost: تكلفة الشحن
    - notes: ملاحظات
    - created_at: تاريخ الطلب
    - updated_at: تاريخ التحديث
    - confirmed_at: تاريخ التأكيد
    - shipped_at: تاريخ الشحن
    - delivered_at: تاريخ التسليم
```

#### 7. نموذج عنصر الطلب (OrderItem)
```python
class OrderItem:
    - id: Primary Key
    - order: ForeignKey → Order
    - product: ForeignKey → Product
    - quantity: الكمية
    - price: السعر
    - total: الإجمالي
```

#### 8. نموذج تاريخ حالة الطلب (OrderStatusHistory)
```python
class OrderStatusHistory:
    - id: Primary Key
    - order: ForeignKey → Order
    - status: الحالة
    - notes: ملاحظات
    - changed_by: ForeignKey → User
    - created_at: تاريخ التغيير
```

### العلاقات بين النماذج
```
User ←→ Customer (OneToOne)
User ←→ Order (OneToMany)
Category ←→ Product (OneToMany)
Product ←→ ProductImage (OneToMany)
Product ←→ OrderItem (OneToMany)
Order ←→ OrderItem (OneToMany)
Order ←→ OrderStatusHistory (OneToMany)
```

---

## 🔐 نظام المصادقة

### مميزات المصادقة

#### 1. تسجيل المستخدمين الجدد
- **الصفحة**: `/accounts/register/`
- **الحقول المطلوبة**: اسم المستخدم، كلمة المرور
- **الحقول الاختيارية**: البريد، الهاتف، العنوان
- **التحقق**: تطابق كلمات المرور، قوة كلمة المرور

#### 2. تسجيل الدخول
- **الصفحة**: `/accounts/login/`
- **المصادقة**: اسم المستخدم + كلمة المرور
- **الأمان**: حماية من هجمات Brute Force
- **إعادة التوجيه**: للصفحة المطلوبة أو الرئيسية

#### 3. إدارة الملف الشخصي
- **الصفحة**: `/accounts/profile/`
- **التحديث**: البيانات الشخصية والعنوان
- **الحماية**: `@login_required` decorator
- **التحقق**: صحة البيانات المدخلة

#### 4. إدارة الطلبات الشخصية
- **الصفحة**: `/accounts/my-orders/`
- **العرض**: طلبات المستخدم فقط
- **الفلترة**: حسب الحالة والتاريخ
- **التفاصيل**: رابط لتفاصيل كل طلب

### إعدادات الأمان
```python
# في settings.py
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# حماية كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    'django.contrib.auth.password_validation.MinimumLengthValidator',
    'django.contrib.auth.password_validation.CommonPasswordValidator',
    'django.contrib.auth.password_validation.NumericPasswordValidator',
]
```

---

## 🛍️ إدارة المنتجات

### هيكل المنتجات

#### 1. الفئات (Categories)
- **الغرض**: تصنيف المنتجات لسهولة التصفح
- **المميزات**:
  - أسماء فريدة مع slugs للـ SEO
  - صور للفئات
  - وصف تفصيلي
  - إمكانية تفعيل/إلغاء تفعيل

#### 2. المنتجات (Products)
- **المعلومات الأساسية**:
  - اسم المنتج ووصف تفصيلي
  - السعر والكمية المتوفرة
  - ربط بفئة واحدة
  - حالة النشاط والتميز

#### 3. صور المنتجات (Product Images)
- **الصورة الرئيسية**: تظهر في قوائم المنتجات
- **صور إضافية**: معرض صور في صفحة المنتج
- **تحسين الصور**: ضغط تلقائي وأحجام متعددة

### واجهات المنتجات

#### صفحة قائمة المنتجات (`/products/`)
```python
# المميزات:
- عرض جميع المنتجات النشطة
- فلترة حسب الفئة
- بحث في أسماء المنتجات
- ترقيم الصفحات (Pagination)
- ترتيب حسب السعر/التاريخ
```

#### صفحة تفاصيل المنتج (`/product/<slug>/`)
```python
# المحتوى:
- معلومات مفصلة عن المنتج
- معرض صور تفاعلي
- زر إضافة للسلة
- منتجات مقترحة
- تقييمات العملاء (مستقبلي)
```

#### صفحة الفئة (`/category/<slug>/`)
```python
# العرض:
- منتجات الفئة المحددة فقط
- معلومات الفئة ووصفها
- نفس مميزات الفلترة والبحث
- breadcrumb navigation
```

---

## 🛒 نظام الطلبات

### دورة حياة الطلب

#### 1. السلة (Shopping Cart)
```python
# الوظائف:
- إضافة منتجات للسلة
- تحديث الكميات
- حذف منتجات
- حساب الإجمالي تلقائياً
- حفظ السلة في الجلسة
```

#### 2. صفحة الدفع (Checkout)
```python
# المراحل:
1. مراجعة السلة
2. إدخال بيانات العميل
3. اختيار طريقة الدفع
4. تأكيد الطلب
5. إنشاء رقم طلب فريد
```

#### 3. حالات الطلب
```python
ORDER_STATUS_CHOICES = [
    ('pending', 'في الانتظار'),
    ('confirmed', 'مؤكد'),
    ('processing', 'قيد التحضير'),
    ('shipped', 'تم الشحن'),
    ('delivered', 'تم التسليم'),
    ('cancelled', 'ملغي'),
    ('returned', 'مرتجع'),
]
```

#### 4. تتبع الطلبات
```python
# المميزات:
- رقم طلب فريد لكل طلب
- تاريخ تفصيلي لتغيير الحالات
- إشعارات للعملاء (مستقبلي)
- تقدير وقت التسليم
```

### AJAX والتفاعل

#### إضافة للسلة
```javascript
// وظيفة إضافة منتج للسلة
function addToCart(productId, quantity) {
    fetch('/orders/add-to-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            'product_id': productId,
            'quantity': quantity
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateCartCount(data.cart_count);
            showNotification('تم إضافة المنتج للسلة', 'success');
        }
    });
}
```

#### تحديث السلة
```javascript
// تحديث كمية منتج في السلة
function updateCartItem(productId, quantity) {
    // منطق مشابه مع endpoint مختلف
    // /orders/update-cart/
}
```

---

## 🎨 واجهة المستخدم

### نظام التصميم

#### 1. نظام الألوان
```css
:root {
    /* الألوان الأساسية */
    --primary-color: #1e3a8a;      /* Navy Blue */
    --secondary-color: #3b82f6;    /* Light Blue */
    --accent-color: #f59e0b;       /* Amber */

    /* ألوان الخلفية */
    --dark-bg: #0f172a;            /* Slate 900 */
    --dark-card: #1e293b;          /* Slate 800 */
    --dark-border: #334155;        /* Slate 700 */

    /* ألوان النص */
    --text-light: #f8fafc;         /* Slate 50 */
    --text-muted: #94a3b8;         /* Slate 400 */
}
```

#### 2. Typography
```css
/* الخطوط */
body {
    font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: var(--text-light);
}

/* العناوين */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    margin-bottom: 1rem;
}
```

#### 3. المكونات (Components)

##### البطاقات (Cards)
```css
.card {
    background: var(--dark-card);
    border: 1px solid var(--dark-border);
    border-radius: 12px;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}
```

##### الأزرار (Buttons)
```css
.btn-primary {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: 500;
    transition: all 0.3s ease;
}
```

### التجاوب (Responsive Design)

#### نقاط التوقف (Breakpoints)
```css
/* Mobile First Approach */
/* Extra Small devices (phones, 576px and down) */
@media (max-width: 575.98px) { }

/* Small devices (landscape phones, 576px and up) */
@media (min-width: 576px) { }

/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) { }

/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) { }

/* Extra large devices (large desktops, 1200px and up) */
@media (min-width: 1200px) { }
```

#### تحسينات الجوال
```css
/* تحسينات خاصة بالجوال */
@media (max-width: 768px) {
    .container {
        padding: 0 15px;
    }

    .card {
        margin-bottom: 1rem;
    }

    .btn {
        width: 100%;
        margin-bottom: 0.5rem;
    }
}
```

---

## 🔒 الأمان والحماية

### مستويات الحماية

#### 1. حماية CSRF
```python
# في جميع النماذج
{% csrf_token %}

# في AJAX requests
headers: {
    'X-CSRFToken': getCookie('csrftoken')
}
```

#### 2. تشفير كلمات المرور
```python
# Django يستخدم PBKDF2 افتراضياً
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
```

#### 3. حماية الصفحات
```python
# استخدام decorators
@login_required
def profile_view(request):
    # كود الـ view

# أو في class-based views
class ProfileView(LoginRequiredMixin, View):
    # كود الـ view
```

#### 4. تنظيف البيانات
```python
# في النماذج
def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        raise ValidationError('هذا البريد مستخدم بالفعل')
    return email
```

#### 5. حماية الملفات
```python
# في settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# تحديد أنواع الملفات المسموحة
ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
```

### أفضل الممارسات الأمنية

#### 1. التحقق من المدخلات
```python
# تنظيف HTML
from django.utils.html import escape
safe_content = escape(user_input)

# التحقق من الأرقام
if not str(quantity).isdigit():
    raise ValidationError('الكمية يجب أن تكون رقم')
```

#### 2. حماية قاعدة البيانات
```python
# استخدام ORM بدلاً من SQL خام
products = Product.objects.filter(category=category_id)

# بدلاً من:
# cursor.execute(f"SELECT * FROM products WHERE category={category_id}")
```

#### 3. إدارة الجلسات
```python
# في settings.py
SESSION_COOKIE_AGE = 1209600  # أسبوعين
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_SECURE = True  # في الإنتاج
SESSION_COOKIE_HTTPONLY = True
```

---

## ⚡ الأداء والتحسين

### تحسينات قاعدة البيانات

#### 1. الفهرسة (Indexing)
```python
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'category']),
            models.Index(fields=['created_at']),
        ]
```

#### 2. تحسين الاستعلامات
```python
# استخدام select_related للعلاقات OneToOne/ForeignKey
products = Product.objects.select_related('category').all()

# استخدام prefetch_related للعلاقات ManyToMany/Reverse ForeignKey
orders = Order.objects.prefetch_related('items__product').all()

# تحديد الحقول المطلوبة فقط
products = Product.objects.only('name', 'price', 'image').all()
```

#### 3. التخزين المؤقت (Caching)
```python
# في views.py
from django.core.cache import cache

def product_list(request):
    cache_key = 'product_list'
    products = cache.get(cache_key)

    if not products:
        products = Product.objects.filter(is_active=True)
        cache.set(cache_key, products, 300)  # 5 دقائق

    return render(request, 'products/list.html', {'products': products})
```

### تحسينات الواجهة الأمامية

#### 1. ضغط الصور
```python
# في models.py
from PIL import Image

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.image:
        img = Image.open(self.image.path)
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)
```

#### 2. تحميل الصور البطيء (Lazy Loading)
```html
<img src="placeholder.jpg" data-src="actual-image.jpg" class="lazy" alt="Product Image">

<script>
// Intersection Observer للتحميل البطيء
const lazyImages = document.querySelectorAll('.lazy');
const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.remove('lazy');
            observer.unobserve(img);
        }
    });
});

lazyImages.forEach(img => imageObserver.observe(img));
</script>
```

#### 3. تجميع وضغط CSS/JS
```python
# في settings.py للإنتاج
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# استخدام أدوات مثل:
# - django-compressor
# - webpack
# - gulp
```
