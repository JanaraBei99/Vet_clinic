from django.db import models


class BaseReference(models.Model):
    name_ru = models.CharField(max_length=100)
    name_kg = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        abstract = True


class RefRole(BaseReference):
    class Meta:
        db_table = 'ref_role'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class RefProductCategory(BaseReference):
    class Meta:
        db_table = 'ref_product_category'
        verbose_name = 'Категория продукции'
        verbose_name_plural = 'Категории продукций'


class RefBreed(BaseReference):
    class Meta:
        db_table = 'ref_breed'
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class RefTypeOfAnimal(BaseReference):
    class Meta:
        db_table = 'ref_type_of_animal'
        verbose_name = 'Вид питомца(животного)'
        verbose_name_plural = 'Виды питомцев(животных)'


class RefProduct(BaseReference):
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(RefProductCategory, models.CASCADE)

    class Meta:
        db_table = 'ref_product'
        verbose_name = 'Медицинский препарат'
        verbose_name_plural = 'Медицинские препараты'


class RefShop(BaseReference):
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey("users.User", models.CASCADE)

    class Meta:
        db_table = 'ref_shop'
        verbose_name = 'Магазин ветеринарных препаратов'
        verbose_name_plural = 'Магазины ветеринарных препаратов'
