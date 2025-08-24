# 🚀 دليل النشر والإنتاج - Deployment Guide

## 📋 فهرس المحتويات

1. [إعداد الإنتاج](#إعداد-الإنتاج)
2. [متطلبات الخادم](#متطلبات-الخادم)
3. [قاعدة البيانات](#قاعدة-البيانات)
4. [الخادم الويب](#الخادم-الويب)
5. [الأمان](#الأمان)
6. [المراقبة](#المراقبة)
7. [النسخ الاحتياطي](#النسخ-الاحتياطي)

---

## ⚙️ إعداد الإنتاج

### 1. إعدادات Django للإنتاج

#### إنشاء ملف settings_production.py
```python
# settings_production.py
from .settings import *

# إعدادات الإنتاج
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'your-server-ip']

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_db',
        'USER': 'ecommerce_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# الأمان
SECRET_KEY = 'your-production-secret-key-here'
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# الملفات الثابتة
STATIC_ROOT = '/var/www/ecommerce/static/'
MEDIA_ROOT = '/var/www/ecommerce/media/'

# البريد الإلكتروني
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'

# التخزين المؤقت
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# السجلات
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/ecommerce/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### 2. متغيرات البيئة
```bash
# .env
SECRET_KEY=your-production-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_URL=redis://localhost:6379/1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

---

## 🖥️ متطلبات الخادم

### المواصفات المطلوبة
```
CPU: 2 cores minimum (4 cores recommended)
RAM: 2GB minimum (4GB recommended)
Storage: 20GB minimum (SSD recommended)
OS: Ubuntu 20.04 LTS or CentOS 8
```

### البرامج المطلوبة
```bash
# تحديث النظام
sudo apt update && sudo apt upgrade -y

# Python و pip
sudo apt install python3 python3-pip python3-venv -y

# PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Redis
sudo apt install redis-server -y

# Nginx
sudo apt install nginx -y

# Supervisor (لإدارة العمليات)
sudo apt install supervisor -y

# أدوات إضافية
sudo apt install git curl wget htop -y
```

---

## 🗄️ قاعدة البيانات

### إعداد PostgreSQL

#### 1. إنشاء قاعدة البيانات والمستخدم
```sql
-- الدخول لـ PostgreSQL
sudo -u postgres psql

-- إنشاء قاعدة البيانات
CREATE DATABASE ecommerce_db;

-- إنشاء مستخدم
CREATE USER ecommerce_user WITH PASSWORD 'your_secure_password';

-- منح الصلاحيات
GRANT ALL PRIVILEGES ON DATABASE ecommerce_db TO ecommerce_user;

-- إعدادات إضافية
ALTER ROLE ecommerce_user SET client_encoding TO 'utf8';
ALTER ROLE ecommerce_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ecommerce_user SET timezone TO 'UTC';

-- الخروج
\q
```

#### 2. إعداد النسخ الاحتياطي التلقائي
```bash
# إنشاء سكريبت النسخ الاحتياطي
sudo nano /usr/local/bin/backup_db.sh

#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/var/backups/ecommerce"
DB_NAME="ecommerce_db"
DB_USER="ecommerce_user"

mkdir -p $BACKUP_DIR
pg_dump -U $DB_USER -h localhost $DB_NAME > $BACKUP_DIR/backup_$DATE.sql
gzip $BACKUP_DIR/backup_$DATE.sql

# حذف النسخ الأقدم من 7 أيام
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +7 -delete

# جعل السكريبت قابل للتنفيذ
sudo chmod +x /usr/local/bin/backup_db.sh

# إضافة مهمة cron للنسخ الاحتياطي اليومي
sudo crontab -e
# إضافة السطر التالي:
0 2 * * * /usr/local/bin/backup_db.sh
```

---

## 🌐 الخادم الويب

### إعداد Nginx

#### 1. إنشاء ملف التكوين
```nginx
# /etc/nginx/sites-available/ecommerce
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;

    # Security Headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

    # Static Files
    location /static/ {
        alias /var/www/ecommerce/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /var/www/ecommerce/media/;
        expires 1y;
        add_header Cache-Control "public";
    }

    # Django Application
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Gzip Compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_proxied expired no-cache no-store private must-revalidate auth;
    gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml+rss;
}
```

#### 2. تفعيل الموقع
```bash
# إنشاء رابط رمزي
sudo ln -s /etc/nginx/sites-available/ecommerce /etc/nginx/sites-enabled/

# اختبار التكوين
sudo nginx -t

# إعادة تشغيل Nginx
sudo systemctl restart nginx
```

### إعداد Gunicorn

#### 1. تثبيت Gunicorn
```bash
pip install gunicorn
```

#### 2. إنشاء ملف التكوين
```python
# gunicorn_config.py
bind = "127.0.0.1:8000"
workers = 3
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2
preload_app = True
```

#### 3. إعداد Supervisor
```ini
# /etc/supervisor/conf.d/ecommerce.conf
[program:ecommerce]
command=/var/www/ecommerce/venv/bin/gunicorn core.wsgi:application -c gunicorn_config.py
directory=/var/www/ecommerce
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/ecommerce/gunicorn.log
environment=DJANGO_SETTINGS_MODULE="core.settings_production"
```

---

## 🔒 الأمان

### 1. جدار الحماية (UFW)
```bash
# تفعيل UFW
sudo ufw enable

# السماح بـ SSH
sudo ufw allow ssh

# السماح بـ HTTP و HTTPS
sudo ufw allow 'Nginx Full'

# حالة الجدار
sudo ufw status
```

### 2. SSL Certificate (Let's Encrypt)
```bash
# تثبيت Certbot
sudo apt install certbot python3-certbot-nginx -y

# الحصول على شهادة SSL
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# تجديد تلقائي
sudo crontab -e
# إضافة السطر التالي:
0 12 * * * /usr/bin/certbot renew --quiet
```

### 3. تحديثات الأمان
```bash
# تحديثات تلقائية
sudo apt install unattended-upgrades -y
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## 📊 المراقبة

### 1. مراقبة الخادم
```bash
# تثبيت htop للمراقبة
sudo apt install htop -y

# مراقبة استخدام القرص
df -h

# مراقبة الذاكرة
free -h

# مراقبة العمليات
ps aux | grep gunicorn
```

### 2. سجلات النظام
```bash
# سجلات Django
tail -f /var/log/ecommerce/django.log

# سجلات Gunicorn
tail -f /var/log/ecommerce/gunicorn.log

# سجلات Nginx
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

# سجلات PostgreSQL
tail -f /var/log/postgresql/postgresql-12-main.log
```

### 3. مراقبة الأداء
```python
# إضافة middleware للمراقبة
# في settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # إضافة middleware مخصص للمراقبة
    'core.middleware.PerformanceMiddleware',
]
```

---

## 💾 النسخ الاحتياطي

### 1. نسخ احتياطي شامل
```bash
#!/bin/bash
# /usr/local/bin/full_backup.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/var/backups/ecommerce"
PROJECT_DIR="/var/www/ecommerce"

mkdir -p $BACKUP_DIR

# نسخ قاعدة البيانات
pg_dump -U ecommerce_user -h localhost ecommerce_db > $BACKUP_DIR/db_$DATE.sql

# نسخ ملفات المشروع
tar -czf $BACKUP_DIR/project_$DATE.tar.gz -C /var/www ecommerce

# نسخ ملفات الوسائط
tar -czf $BACKUP_DIR/media_$DATE.tar.gz -C /var/www/ecommerce media

# ضغط نسخة قاعدة البيانات
gzip $BACKUP_DIR/db_$DATE.sql

# حذف النسخ الأقدم من 30 يوم
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -delete
find $BACKUP_DIR -name "*.sql.gz" -mtime +30 -delete

echo "Backup completed: $DATE"
```

### 2. استعادة النسخ الاحتياطية
```bash
#!/bin/bash
# استعادة قاعدة البيانات
gunzip backup_file.sql.gz
psql -U ecommerce_user -h localhost ecommerce_db < backup_file.sql

# استعادة ملفات المشروع
tar -xzf project_backup.tar.gz -C /var/www/

# استعادة ملفات الوسائط
tar -xzf media_backup.tar.gz -C /var/www/ecommerce/
```

---

## 🚀 خطوات النشر

### 1. النشر الأولي
```bash
# 1. رفع الكود للخادم
git clone https://github.com/your-repo/ecommerce.git /var/www/ecommerce
cd /var/www/ecommerce

# 2. إنشاء البيئة الافتراضية
python3 -m venv venv
source venv/bin/activate

# 3. تثبيت المتطلبات
pip install -r requirements.txt

# 4. إعداد قاعدة البيانات
python manage.py migrate --settings=core.settings_production

# 5. جمع الملفات الثابتة
python manage.py collectstatic --noinput --settings=core.settings_production

# 6. إنشاء مستخدم إداري
python manage.py createsuperuser --settings=core.settings_production

# 7. تشغيل الخدمات
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start ecommerce
```

### 2. التحديثات
```bash
#!/bin/bash
# deploy.sh - سكريبت التحديث

cd /var/www/ecommerce

# سحب آخر التحديثات
git pull origin main

# تفعيل البيئة الافتراضية
source venv/bin/activate

# تثبيت المتطلبات الجديدة
pip install -r requirements.txt

# تطبيق migrations
python manage.py migrate --settings=core.settings_production

# جمع الملفات الثابتة
python manage.py collectstatic --noinput --settings=core.settings_production

# إعادة تشغيل التطبيق
sudo supervisorctl restart ecommerce

# إعادة تحميل Nginx
sudo nginx -s reload

echo "Deployment completed successfully!"
```

---

## 📋 قائمة التحقق

### قبل النشر
- [ ] اختبار جميع الوظائف في بيئة التطوير
- [ ] تحديث requirements.txt
- [ ] إعداد متغيرات البيئة
- [ ] اختبار النسخ الاحتياطي والاستعادة
- [ ] مراجعة إعدادات الأمان

### بعد النشر
- [ ] اختبار الموقع في المتصفح
- [ ] التحقق من عمل SSL
- [ ] اختبار تسجيل الدخول والتسجيل
- [ ] اختبار إضافة منتجات للسلة
- [ ] اختبار إتمام الطلبات
- [ ] مراجعة السجلات للأخطاء
- [ ] اختبار النسخ الاحتياطي

---

**آخر تحديث:** ديسمبر 2024
