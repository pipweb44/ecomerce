# 🗺️ خريطة الموقع - Site Map

## 📋 جميع URLs والصفحات المتاحة

### 🏠 الصفحات الرئيسية

| الصفحة | URL | الوصف | المصادقة |
|--------|-----|--------|----------|
| الصفحة الرئيسية | `/` | عرض المنتجات المميزة والفئات | لا |
| قائمة المنتجات | `/products/` | جميع المنتجات مع فلترة وبحث | لا |
| تفاصيل المنتج | `/product/<slug>/` | صفحة المنتج مع التفاصيل | لا |
| منتجات الفئة | `/category/<slug>/` | منتجات فئة محددة | لا |

### 🛒 نظام الطلبات والسلة

| الصفحة | URL | الوصف | المصادقة |
|--------|-----|--------|----------|
| السلة | `/orders/cart/` | عرض محتويات السلة | لا |
| إتمام الطلب | `/orders/checkout/` | صفحة الدفع وإتمام الطلب | لا |
| نجاح الطلب | `/orders/success/` | تأكيد إتمام الطلب | لا |
| تتبع الطلب | `/orders/track/` | البحث عن طلب وتتبعه | لا |

### 🔐 نظام المصادقة

| الصفحة | URL | الوصف | المصادقة |
|--------|-----|--------|----------|
| تسجيل الدخول | `/accounts/login/` | صفحة تسجيل الدخول | لا |
| التسجيل | `/accounts/register/` | إنشاء حساب جديد | لا |
| تسجيل الخروج | `/accounts/logout/` | تسجيل خروج المستخدم | مطلوبة |
| الملف الشخصي | `/accounts/profile/` | إدارة البيانات الشخصية | مطلوبة |
| طلباتي | `/accounts/my-orders/` | طلبات المستخدم | مطلوبة |
| تفاصيل الطلب | `/accounts/order/<uuid>/` | تفاصيل طلب محدد | مطلوبة |

### 👨‍💼 لوحة الإدارة

| الصفحة | URL | الوصف | المصادقة |
|--------|-----|--------|----------|
| لوحة الإدارة | `/admin/` | الصفحة الرئيسية للإدارة | إدارية |
| إدارة المنتجات | `/admin/products/product/` | قائمة وإدارة المنتجات | إدارية |
| إضافة منتج | `/admin/products/product/add/` | إضافة منتج جديد | إدارية |
| تعديل منتج | `/admin/products/product/<id>/change/` | تعديل منتج موجود | إدارية |
| إدارة الفئات | `/admin/products/category/` | قائمة وإدارة الفئات | إدارية |
| إدارة الطلبات | `/admin/orders/order/` | قائمة وإدارة الطلبات | إدارية |
| تفاصيل الطلب | `/admin/orders/order/<id>/change/` | تفاصيل وتعديل طلب | إدارية |
| إدارة العملاء | `/admin/customers/customer/` | قائمة وإدارة العملاء | إدارية |
| إدارة المستخدمين | `/admin/auth/user/` | قائمة وإدارة المستخدمين | إدارية |

---

## 🔗 AJAX Endpoints

### 🛒 عمليات السلة

| العملية | Method | URL | الوصف |
|---------|--------|-----|--------|
| إضافة للسلة | POST | `/orders/add-to-cart/` | إضافة منتج للسلة |
| تحديث السلة | POST | `/orders/update-cart/` | تحديث كمية منتج |
| حذف من السلة | POST | `/orders/remove-from-cart/` | حذف منتج من السلة |
| مسح السلة | POST | `/orders/clear-cart/` | مسح جميع محتويات السلة |

### 📊 عمليات البيانات

| العملية | Method | URL | الوصف |
|---------|--------|-----|--------|
| بحث المنتجات | GET | `/products/?search=<query>` | البحث في المنتجات |
| فلترة الفئة | GET | `/products/?category=<uuid>` | فلترة حسب الفئة |
| ترقيم الصفحات | GET | `/products/?page=<number>` | التنقل بين الصفحات |

---

## 📱 هيكل التنقل

### القائمة الرئيسية
```
الرئيسية (/)
├── المنتجات (/products/)
│   ├── فئة 1 (/category/electronics/)
│   ├── فئة 2 (/category/clothing/)
│   └── فئة 3 (/category/books/)
├── السلة (/orders/cart/)
├── تتبع الطلب (/orders/track/)
└── الحساب
    ├── تسجيل الدخول (/accounts/login/)
    ├── التسجيل (/accounts/register/)
    ├── الملف الشخصي (/accounts/profile/)
    └── طلباتي (/accounts/my-orders/)
```

### قائمة المستخدم المسجل
```
مرحباً [اسم المستخدم] ▼
├── الملف الشخصي (/accounts/profile/)
├── طلباتي (/accounts/my-orders/)
└── تسجيل الخروج (/accounts/logout/)
```

---

## 🔍 URLs بالتفصيل

### Products App URLs
```python
# products/urls.py
urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.product_list_view, name='product_list'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('category/<slug:slug>/', views.category_view, name='category_detail'),
]
```

### Orders App URLs
```python
# orders/urls.py
urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('success/', views.order_success_view, name='order_success'),
    path('track/', views.track_order, name='track_order'),
]
```

### Accounts App URLs
```python
# accounts/urls.py
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('my-orders/', views.my_orders_view, name='my_orders'),
    path('order/<uuid:order_id>/', views.order_detail_view, name='order_detail'),
]
```

---

## 🎯 URL Patterns والمعاملات

### معاملات URL الشائعة

#### Slug Parameters
```
/product/<slug:slug>/
/category/<slug:slug>/
```
- **النوع:** SlugField
- **المثال:** `/product/samsung-galaxy-s21/`
- **الاستخدام:** للمنتجات والفئات

#### UUID Parameters
```
/accounts/order/<uuid:order_id>/
```
- **النوع:** UUIDField
- **المثال:** `/accounts/order/123e4567-e89b-12d3-a456-426614174000/`
- **الاستخدام:** للطلبات والعملاء

#### Query Parameters
```
/products/?search=laptop&category=electronics&page=2
```
- **search:** البحث في أسماء المنتجات
- **category:** UUID الفئة للفلترة
- **page:** رقم الصفحة للترقيم

---

## 🔒 مستويات الحماية

### صفحات عامة (Public)
- الصفحة الرئيسية
- قائمة المنتجات
- تفاصيل المنتج
- السلة
- تتبع الطلب
- تسجيل الدخول/التسجيل

### صفحات محمية (Login Required)
- الملف الشخصي
- طلباتي
- تفاصيل الطلب الشخصي

### صفحات إدارية (Admin Required)
- جميع صفحات `/admin/`
- إدارة المنتجات والطلبات
- إدارة المستخدمين

---

## 📊 إحصائيات URLs

| التطبيق | عدد URLs | النوع |
|---------|----------|-------|
| Products | 4 | عامة |
| Orders | 7 | مختلطة |
| Accounts | 6 | محمية |
| Admin | 20+ | إدارية |
| **المجموع** | **37+** | **مختلطة** |

---

## 🔄 إعادة التوجيه (Redirects)

### إعادة التوجيه التلقائي
```python
# بعد تسجيل الدخول
LOGIN_REDIRECT_URL = '/'

# بعد تسجيل الخروج
LOGOUT_REDIRECT_URL = '/'

# بعد إتمام الطلب
return redirect('orders:order_success')

# بعد التسجيل الناجح
return redirect('products:home')
```

### إعادة التوجيه المشروطة
```python
# إعادة توجيه المستخدمين المسجلين
if request.user.is_authenticated:
    return redirect('accounts:profile')

# إعادة توجيه بناءً على الصلاحيات
if request.user.is_staff:
    return redirect('admin:index')
```

---

## 🌐 SEO و URLs الصديقة

### بنية URLs المحسنة
```
✅ الصحيح:
/product/samsung-galaxy-s21/
/category/smartphones/

❌ الخطأ:
/product/123/
/category/1/
```

### Meta Tags للصفحات
```html
<!-- الصفحة الرئيسية -->
<title>متجري الإلكتروني - أفضل المنتجات بأسعار منافسة</title>
<meta name="description" content="تسوق أحدث المنتجات الإلكترونية والأزياء والكتب بأفضل الأسعار">

<!-- صفحة المنتج -->
<title>{{ product.name }} - متجري الإلكتروني</title>
<meta name="description" content="{{ product.description|truncatewords:20 }}">

<!-- صفحة الفئة -->
<title>{{ category.name }} - متجري الإلكتروني</title>
<meta name="description" content="تسوق أفضل منتجات {{ category.name }} بأسعار منافسة">
```

---

## 📱 URLs للجوال

جميع URLs تعمل بشكل متجاوب على الأجهزة المحمولة مع نفس الروابط:

### تحسينات الجوال
- **تصميم متجاوب:** جميع الصفحات
- **تحميل سريع:** ضغط الصور والملفات
- **تنقل سهل:** قوائم مبسطة
- **لمس مريح:** أزرار كبيرة

---

## 🔮 URLs المستقبلية (مخطط لها)

### مميزات قادمة
```
/api/v1/products/          # REST API
/wishlist/                 # قائمة الأمنيات
/compare/                  # مقارنة المنتجات
/reviews/                  # تقييمات المنتجات
/coupons/                  # كوبونات الخصم
/notifications/            # الإشعارات
/support/                  # الدعم الفني
```

### تحسينات مخططة
- **API RESTful** كامل
- **نظام تقييمات** المنتجات
- **قائمة أمنيات** شخصية
- **نظام إشعارات** متقدم
- **دعم فني** تفاعلي

---

**آخر تحديث:** ديسمبر 2024  
**إجمالي URLs:** 37+ رابط  
**التغطية:** 100% من الوظائف المطلوبة
