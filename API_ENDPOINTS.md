# 🔗 API Endpoints Documentation

## 📋 فهرس المحتويات

1. [نظرة عامة](#نظرة-عامة)
2. [المصادقة](#المصادقة)
3. [المنتجات](#المنتجات)
4. [الطلبات والسلة](#الطلبات-والسلة)
5. [إدارة الحساب](#إدارة-الحساب)
6. [الإدارة](#الإدارة)
7. [رموز الاستجابة](#رموز-الاستجابة)

---

## 🌐 نظرة عامة

### Base URL
```
Development: http://127.0.0.1:8000
Production: https://yourdomain.com
```

### تنسيق الاستجابة
جميع الاستجابات بتنسيق JSON أو HTML حسب النوع:
- **Web Pages**: HTML Templates
- **AJAX Requests**: JSON Response
- **API Calls**: JSON Response

### Headers المطلوبة
```http
Content-Type: application/json
X-CSRFToken: [csrf_token]  # للطلبات POST/PUT/DELETE
```

---

## 🔐 المصادقة (Authentication)

### تسجيل الدخول
```http
POST /accounts/login/
```

**Parameters:**
```json
{
    "username": "string",
    "password": "string"
}
```

**Response (Success):**
```http
HTTP/1.1 302 Found
Location: /
Set-Cookie: sessionid=...
```

**Response (Error):**
```html
<!-- صفحة تسجيل الدخول مع رسائل الخطأ -->
```

---

### تسجيل مستخدم جديد
```http
POST /accounts/register/
```

**Parameters:**
```json
{
    "username": "string",
    "password1": "string",
    "password2": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string",
    "phone": "string",
    "address": "string",
    "city": "string"
}
```

**Response (Success):**
```http
HTTP/1.1 302 Found
Location: /
```

---

### تسجيل الخروج
```http
POST /accounts/logout/
```

**Response:**
```http
HTTP/1.1 302 Found
Location: /
```

---

### الملف الشخصي
```http
GET /accounts/profile/
```

**Authentication:** Required

**Response:**
```html
<!-- صفحة الملف الشخصي -->
```

---

### تحديث الملف الشخصي
```http
POST /accounts/profile/
```

**Authentication:** Required

**Parameters:**
```json
{
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "phone": "string",
    "address": "string",
    "city": "string"
}
```

---

## 🛍️ المنتجات (Products)

### قائمة جميع المنتجات
```http
GET /products/
```

**Query Parameters:**
- `category` (optional): UUID - فلترة حسب الفئة
- `search` (optional): string - البحث في أسماء المنتجات
- `page` (optional): integer - رقم الصفحة

**Example:**
```http
GET /products/?category=123e4567-e89b-12d3-a456-426614174000&search=laptop&page=2
```

**Response:**
```html
<!-- صفحة قائمة المنتجات -->
```

---

### تفاصيل منتج محدد
```http
GET /product/<slug>/
```

**Parameters:**
- `slug`: string - الرابط المختصر للمنتج

**Example:**
```http
GET /product/samsung-galaxy-s21/
```

**Response:**
```html
<!-- صفحة تفاصيل المنتج -->
```

---

### منتجات فئة محددة
```http
GET /category/<slug>/
```

**Parameters:**
- `slug`: string - الرابط المختصر للفئة

**Example:**
```http
GET /category/smartphones/
```

**Response:**
```html
<!-- صفحة منتجات الفئة -->
```

---

## 🛒 الطلبات والسلة (Orders & Cart)

### عرض السلة
```http
GET /orders/cart/
```

**Response:**
```html
<!-- صفحة السلة -->
```

---

### إضافة منتج للسلة
```http
POST /orders/add-to-cart/
```

**Parameters:**
```json
{
    "product_id": "uuid",
    "quantity": "integer"
}
```

**Response (Success):**
```json
{
    "success": true,
    "message": "تم إضافة المنتج للسلة",
    "cart_count": 3,
    "cart_total": "299.99"
}
```

**Response (Error):**
```json
{
    "success": false,
    "message": "المنتج غير متوفر",
    "error_code": "OUT_OF_STOCK"
}
```

---

### تحديث كمية منتج في السلة
```http
POST /orders/update-cart/
```

**Parameters:**
```json
{
    "product_id": "uuid",
    "quantity": "integer"
}
```

**Response:**
```json
{
    "success": true,
    "message": "تم تحديث السلة",
    "cart_count": 2,
    "cart_total": "199.99",
    "item_total": "99.99"
}
```

---

### حذف منتج من السلة
```http
POST /orders/remove-from-cart/
```

**Parameters:**
```json
{
    "product_id": "uuid"
}
```

**Response:**
```json
{
    "success": true,
    "message": "تم حذف المنتج من السلة",
    "cart_count": 1,
    "cart_total": "99.99"
}
```

---

### صفحة الدفع
```http
GET /orders/checkout/
```

**Response:**
```html
<!-- صفحة إتمام الطلب -->
```

---

### إتمام الطلب
```http
POST /orders/checkout/
```

**Parameters:**
```json
{
    "customer_name": "string",
    "customer_email": "string",
    "customer_phone": "string",
    "shipping_address": "string",
    "shipping_city": "string",
    "shipping_postal_code": "string",
    "notes": "string"
}
```

**Response (Success):**
```http
HTTP/1.1 302 Found
Location: /orders/success/
```

---

### صفحة نجاح الطلب
```http
GET /orders/success/
```

**Response:**
```html
<!-- صفحة تأكيد الطلب -->
```

---

### تتبع الطلب
```http
GET /orders/track/
```

**Response:**
```html
<!-- صفحة تتبع الطلب -->
```

---

### البحث عن طلب
```http
POST /orders/track/
```

**Parameters:**
```json
{
    "order_number": "string"
}
```

**Response:**
```html
<!-- صفحة تفاصيل الطلب أو رسالة خطأ -->
```

---

## 👤 إدارة الحساب (Account Management)

### طلبات المستخدم
```http
GET /accounts/my-orders/
```

**Authentication:** Required

**Response:**
```html
<!-- صفحة طلبات المستخدم -->
```

---

### تفاصيل طلب محدد
```http
GET /accounts/order/<order_id>/
```

**Authentication:** Required

**Parameters:**
- `order_id`: UUID - معرف الطلب

**Response:**
```html
<!-- صفحة تفاصيل الطلب -->
```

**Security Note:** المستخدم يمكنه رؤية طلباته فقط

---

## 🔧 الإدارة (Admin)

### لوحة الإدارة
```http
GET /admin/
```

**Authentication:** Admin Required

**Response:**
```html
<!-- لوحة إدارة Django Jazzmin -->
```

---

### إدارة المنتجات
```http
GET /admin/products/product/
POST /admin/products/product/add/
GET /admin/products/product/<id>/change/
POST /admin/products/product/<id>/delete/
```

---

### إدارة الطلبات
```http
GET /admin/orders/order/
GET /admin/orders/order/<id>/change/
```

---

### إدارة العملاء
```http
GET /admin/customers/customer/
GET /admin/customers/customer/<id>/change/
```

---

## 📊 رموز الاستجابة (Response Codes)

### رموز النجاح
- **200 OK**: طلب ناجح
- **201 Created**: تم إنشاء المورد بنجاح
- **302 Found**: إعادة توجيه

### رموز الخطأ
- **400 Bad Request**: بيانات غير صحيحة
- **401 Unauthorized**: غير مصرح
- **403 Forbidden**: ممنوع
- **404 Not Found**: غير موجود
- **500 Internal Server Error**: خطأ في الخادم

---

## 🔍 أمثلة عملية

### مثال: إضافة منتج للسلة باستخدام JavaScript

```javascript
async function addToCart(productId, quantity = 1) {
    try {
        const response = await fetch('/orders/add-to-cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                product_id: productId,
                quantity: quantity
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // تحديث عداد السلة
            document.getElementById('cart-count').textContent = data.cart_count;
            
            // إظهار رسالة نجاح
            showNotification(data.message, 'success');
        } else {
            // إظهار رسالة خطأ
            showNotification(data.message, 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        showNotification('حدث خطأ غير متوقع', 'error');
    }
}

// دالة مساعدة للحصول على CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
```

### مثال: تسجيل دخول باستخدام Fetch API

```javascript
async function login(username, password) {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    
    try {
        const response = await fetch('/accounts/login/', {
            method: 'POST',
            body: formData
        });
        
        if (response.redirected) {
            // تم تسجيل الدخول بنجاح
            window.location.href = response.url;
        } else {
            // فشل تسجيل الدخول
            const html = await response.text();
            // عرض رسائل الخطأ
        }
    } catch (error) {
        console.error('Login error:', error);
    }
}
```

---

## 📝 ملاحظات مهمة

### الأمان
- جميع طلبات POST/PUT/DELETE تتطلب CSRF token
- الصفحات المحمية تتطلب تسجيل دخول
- المستخدمون يرون بياناتهم فقط

### الأداء
- استخدم pagination للقوائم الطويلة
- الصور محسنة تلقائياً
- التخزين المؤقت مفعل للبيانات الثابتة

### التطوير
- جميع URLs تدعم trailing slash
- استخدم slugs للـ SEO
- رسائل الخطأ باللغة العربية

---

**آخر تحديث:** ديسمبر 2024
