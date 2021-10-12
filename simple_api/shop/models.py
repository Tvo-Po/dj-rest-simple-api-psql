from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
    slug = models.SlugField(max_length=100, default='not_change_if_dont_want_custom')
    trade_mark = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    manufacture_date = models.DateField()
    expiration_date = models.DateField()
    shop = models.ManyToManyField('Shop', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == 'not_change_if_dont_want_custom':
            self.slug = f'{self.trade_mark}-'.lower().replace(' ', '-') + \
                        f'{self.name}-'.lower().replace(' ', '-') + \
                        f'{self.weight}'.lower().replace('.', '_')
        super(Product, self).save(*args, **kwargs)


class Shop(models.Model):
    slug = models.SlugField(max_length=100, default='not_change_if_dont_want_custom')
    trade_company = models.ForeignKey('TradeCompany', models.CASCADE, related_name='shops')
    area = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    floor_number = models.IntegerField(default=1)
    city = models.CharField(max_length=200)
    street_name = models.CharField(max_length=200)
    house_number = models.CharField(max_length=50)

    def __str__(self):
        return f'Shop of {self.trade_company.name} located in {self.city}, {self.street_name}, {self.house_number}'

    def save(self, *args, **kwargs):
        if self.slug == 'not_change_if_dont_want_custom':
            self.slug = f'{self.trade_company.name}-'.lower().replace(' ', '-') + \
                        f'{self.street_name}-'.lower().replace(' ', '-') + \
                        f'{self.house_number}'.lower().replace(' ', '_')
        if self.floor_number < 1 or self.floor_number > 200:
            raise ValidationError('Unacceptable floor number')
        if self.area < 0:
            raise ValidationError('Unacceptable area')
        if not self.area:
            self.area = None
        super(Shop, self).save(*args, **kwargs)


class TradeCompany(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'trade companies'

    def __str__(self):
        return self.name
