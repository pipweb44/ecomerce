from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    help = 'إصلاح slugs للفئات والمنتجات'

    def handle(self, *args, **options):
        self.stdout.write('إصلاح slugs...')

        # إصلاح slugs للفئات
        categories = Category.objects.all()
        for category in categories:
            self.stdout.write(f'Category: {category.name}, Slug: "{category.slug}"')
            if not category.slug or category.slug.strip() == '':
                category.slug = None  # سيتم إنشاء slug جديد في save()
                category.save()
                self.stdout.write(f'Fixed slug for category {category.name}: {category.slug}')

        # إصلاح slugs للمنتجات
        products = Product.objects.all()
        for product in products:
            self.stdout.write(f'Product: {product.name}, Slug: "{product.slug}"')
            if not product.slug or product.slug.strip() == '':
                product.slug = None  # سيتم إنشاء slug جديد في save()
                product.save()
                self.stdout.write(f'Fixed slug for product {product.name}: {product.slug}')

        self.stdout.write(
            self.style.SUCCESS('تم إصلاح جميع slugs بنجاح!')
        )
