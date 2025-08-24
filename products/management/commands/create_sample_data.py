from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'إنشاء بيانات تجريبية للمنتجات والفئات'

    def handle(self, *args, **options):
        self.stdout.write('إنشاء البيانات التجريبية...')

        # إنشاء الفئات
        categories_data = [
            {'name': 'الإلكترونيات', 'description': 'أجهزة إلكترونية متنوعة'},
            {'name': 'الملابس', 'description': 'ملابس رجالية ونسائية'},
            {'name': 'المنزل والحديقة', 'description': 'أدوات منزلية ومستلزمات الحديقة'},
            {'name': 'الكتب', 'description': 'كتب متنوعة في جميع المجالات'},
            {'name': 'الرياضة', 'description': 'معدات ومستلزمات رياضية'},
            {'name': 'الجمال والعناية', 'description': 'منتجات التجميل والعناية الشخصية'},
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'تم إنشاء فئة: {category.name}')

        # إنشاء المنتجات
        products_data = [
            # الإلكترونيات
            {
                'name': 'هاتف ذكي سامسونج جالاكسي',
                'category': categories[0],
                'description': 'هاتف ذكي متطور بكاميرا عالية الجودة وشاشة AMOLED',
                'short_description': 'هاتف ذكي متطور بمواصفات عالية',
                'price': Decimal('2500.00'),
                'discount_price': Decimal('2200.00'),
                'stock_quantity': 15,
                'is_featured': True,
            },
            {
                'name': 'لابتوب ديل انسبايرون',
                'category': categories[0],
                'description': 'لابتوب قوي للعمل والألعاب مع معالج Intel Core i7',
                'short_description': 'لابتوب قوي للعمل والألعاب',
                'price': Decimal('4500.00'),
                'stock_quantity': 8,
                'is_featured': True,
            },
            {
                'name': 'سماعات بلوتوث لاسلكية',
                'category': categories[0],
                'description': 'سماعات عالية الجودة مع إلغاء الضوضاء',
                'short_description': 'سماعات لاسلكية عالية الجودة',
                'price': Decimal('350.00'),
                'discount_price': Decimal('280.00'),
                'stock_quantity': 25,
            },
            
            # الملابس
            {
                'name': 'قميص قطني رجالي',
                'category': categories[1],
                'description': 'قميص قطني عالي الجودة مناسب للعمل والمناسبات',
                'short_description': 'قميص قطني رجالي أنيق',
                'price': Decimal('120.00'),
                'stock_quantity': 30,
                'is_featured': True,
            },
            {
                'name': 'فستان نسائي أنيق',
                'category': categories[1],
                'description': 'فستان أنيق مناسب للمناسبات الخاصة',
                'short_description': 'فستان نسائي للمناسبات',
                'price': Decimal('250.00'),
                'discount_price': Decimal('200.00'),
                'stock_quantity': 20,
            },
            
            # المنزل والحديقة
            {
                'name': 'طقم أواني طبخ',
                'category': categories[2],
                'description': 'طقم أواني طبخ من الستانلس ستيل عالي الجودة',
                'short_description': 'طقم أواني طبخ متكامل',
                'price': Decimal('450.00'),
                'stock_quantity': 12,
                'is_featured': True,
            },
            {
                'name': 'مكنسة كهربائية',
                'category': categories[2],
                'description': 'مكنسة كهربائية قوية ومتعددة الاستخدامات',
                'short_description': 'مكنسة كهربائية قوية',
                'price': Decimal('380.00'),
                'stock_quantity': 10,
            },
            
            # الكتب
            {
                'name': 'كتاب تطوير الذات',
                'category': categories[3],
                'description': 'كتاب ملهم في تطوير الذات والنجاح',
                'short_description': 'كتاب تطوير الذات والنجاح',
                'price': Decimal('45.00'),
                'stock_quantity': 50,
            },
            {
                'name': 'رواية أدبية',
                'category': categories[3],
                'description': 'رواية أدبية شيقة من أفضل الكتاب',
                'short_description': 'رواية أدبية شيقة',
                'price': Decimal('35.00'),
                'discount_price': Decimal('28.00'),
                'stock_quantity': 40,
            },
            
            # الرياضة
            {
                'name': 'دراجة هوائية',
                'category': categories[4],
                'description': 'دراجة هوائية عالية الجودة مناسبة لجميع الأعمار',
                'short_description': 'دراجة هوائية عالية الجودة',
                'price': Decimal('850.00'),
                'stock_quantity': 6,
                'is_featured': True,
            },
            {
                'name': 'حذاء رياضي',
                'category': categories[4],
                'description': 'حذاء رياضي مريح ومناسب للجري والتمارين',
                'short_description': 'حذاء رياضي مريح',
                'price': Decimal('180.00'),
                'stock_quantity': 35,
            },
            
            # الجمال والعناية
            {
                'name': 'كريم مرطب للوجه',
                'category': categories[5],
                'description': 'كريم مرطب طبيعي للوجه مناسب لجميع أنواع البشرة',
                'short_description': 'كريم مرطب طبيعي للوجه',
                'price': Decimal('85.00'),
                'stock_quantity': 45,
            },
            {
                'name': 'شامبو طبيعي',
                'category': categories[5],
                'description': 'شامبو طبيعي خالي من المواد الكيميائية الضارة',
                'short_description': 'شامبو طبيعي للشعر',
                'price': Decimal('55.00'),
                'discount_price': Decimal('45.00'),
                'stock_quantity': 60,
            },
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'تم إنشاء منتج: {product.name}')

        self.stdout.write(
            self.style.SUCCESS('تم إنشاء البيانات التجريبية بنجاح!')
        )
