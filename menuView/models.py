from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255) #название блюда
    gramms = models.TextField(blank=True, null=True) #граммы блюда
    description = models.TextField(blank=True, null=True) #список используемых ингредиентов
    price = models.DecimalField(max_digits=5, decimal_places=2) #цена блюда
    created_at = models.DateTimeField(auto_now_add=True) #дата создания блюда
    updated_at = models.DateTimeField(auto_now=True) #дата обновления блюда
    
    menu_type_choices = [
        ('main', 'Основное меню'),
        ('banquet', 'Банкетное меню'),
    ] #типы меню
    menu_type = models.CharField(max_length=20, choices=menu_type_choices, default='main') #тип меню

    types_available_at_restaurant = [
        ('available', 'Доступно'),
        ('unavailable', 'Недоступно'),
        ('coming_soon', 'Скоро будет'),
        ('special', 'Специальное'),
        ('seasonal', 'Сезонное'),
        ('popular', 'Популярное'),
        ('new', 'Новое'),
    ] #типы блюд, которые доступны в ресторане

    available_at_restaurant = models.CharField(max_length=255, choices=types_available_at_restaurant, default='available') #типы блюд, которые доступны в ресторане

    type_group_menu = [
        ('salad', 'Салаты'),
        ('cold_dish', 'Холодные закуски'),
        ('soup', 'Супы'),
        ('hot_dish', 'Горячее'),
        ('garnish', 'Гарниры, соусы'),
        ('beer', 'К пиву'),
        ('dessert', 'Десерты'),
        ('konditer', 'Кондитерские изделия'),
        ('drink', 'Горячие напитки'),
        ('non_alcoholic_drink', 'Безалкогольные напитки'),
        ('sok', 'Соки. Напитки'),
        ('energetic_drink', 'Энергетический напиток'),
        ('other', 'Другое'),
    ] #типы групп блюд
    type_group_menu = models.CharField(max_length=255, choices=type_group_menu, default='other') #тип группы блюд

    image_url = models.ImageField(upload_to='menu_images/', blank=True, null=True) #изображение блюда

    what_cuisine_dish = [
        ('traditional', 'Традиционная'),
        ('belarussian', 'Белорусская кухня')
    ] #типы кухни блюда

    what_cuisine_dish = models.CharField(max_length=255, choices=what_cuisine_dish, default='traditional') #тип кухни блюда

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name