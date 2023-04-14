from django.db.models import (Model, CharField, SlugField,
                              Index, IntegerField, ForeignKey,
                              CASCADE, ImageField, BooleanField)


class Category(Model):

    name = CharField(
        'Название',
        max_length=64,
    )
    slug = SlugField(
        'URL',
        unique=True
    )

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Category: {self.pk}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
        indexes = [
            Index(fields=('slug',))
        ]


class Product(Model):

    name = CharField(
        'Название',
        max_length=128
    )
    price = IntegerField('Цена')
    kkal = IntegerField('KKAL')
    bju = IntegerField('BJU')
    title = CharField(
        'Описание',
        max_length=512
    )
    slug = SlugField(
        'URL',
        unique=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Product: {self.pk}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        indexes = [
            Index(fields=('slug',))
        ]


class ProductCategory(Model):

    category = ForeignKey(
        Category,
        on_delete=CASCADE,
        verbose_name='Категория',
        related_name='category_products'
    )
    product = ForeignKey(
        Product,
        on_delete=CASCADE,
        verbose_name='Продукт',
        related_name='product_categories'
    )

    def __str__(self):
        return f'{self.pk}'

    def __repr__(self):
        return f'Product Category: {self.pk}'

    class Meta:
        verbose_name = 'Категория и продукт'
        verbose_name_plural = 'Категории и продукты'


class ProductsPhoto(Model):

    product = ForeignKey(
        Product,
        on_delete=CASCADE,
        verbose_name='Продукт',
        related_name='product_photos'
    )
    photo = ImageField(
        'Фото',
        upload_to='photos/products'
    )

    def __str__(self):
        return f'{self.pk}'

    def __repr__(self):
        return f'Product photos: {self.pk}'

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фотографии продуктов'


class Tags(Model):

    name = CharField(
        'Название',
        max_length=64,
    )
    slug = SlugField(
        'URL',
        unique=True
    )

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Tags: {self.pk}'

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class ProductTags(Model):

    tag = ForeignKey(
        Tags,
        on_delete=CASCADE,
        verbose_name='Тэг',
        related_name='tag_products'
    )
    product = ForeignKey(
        Product,
        on_delete=CASCADE,
        verbose_name='Продукт',
        related_name='product_tags'
    )

    def __str__(self):
        return f'{self.pk}'

    def __repr__(self):
        return f'Product Tag: {self.pk}'

    class Meta:
        verbose_name = 'Тэг продукта'
        verbose_name_plural = 'Тэги продуктов'


class Sales(Model):

    name = CharField(
        'Название',
        max_length=128,
    )
    active = BooleanField(
        'Статус активности',
        default=True
    )
    short_title = CharField(
        'Краткое описание',
        max_length=128
    )

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Sales: {self.pk}'

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['name']
        indexes = [
            Index(fields=('name',))
        ]


class SalesProducts(Model):

    sale = ForeignKey(
        Sales,
        on_delete=CASCADE,
        verbose_name='Акция',
        related_name='sale_products'
    )
    product = ForeignKey(
        Product,
        on_delete=CASCADE,
        verbose_name='Продукт',
        related_name='product_sales'
    )

    def __str__(self):
        return f'{self.pk}'

    def __repr__(self):
        return f'Product sale: {self.pk}'

    class Meta:
        verbose_name = 'Акция продукта'
        verbose_name_plural = 'Акции продуктов'