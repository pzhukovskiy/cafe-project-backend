"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from menuView.models import Menu
from feedback.models import Feedback
from django.core.exceptions import ObjectDoesNotExist
from menuView.schemas import MenuSchema, MenuResponseSchema, FeedbackSchema, FeedbackResponseSchema
from django.conf import settings
from django.conf.urls.static import static

from collections import defaultdict
from django.http import JsonResponse
from ninja.files import UploadedFile

api = NinjaAPI()

#создание блюда
@api.post('/menu', response=MenuResponseSchema, tags=['Меню'])
def create_menu(request, menu: MenuSchema):
    data = menu.dict()
    menu_obj = Menu.objects.create(**data)  # type: ignore
    return menu_obj

#получение всего меню с группировкой по типам
@api.get('/menu', tags=['Меню'])
def get_menu(request):
    menu_items = Menu.objects.all()  # type: ignore
    result = {}
    
    # Группируем по типу меню
    for item in menu_items:
        menu_type_name = 'Основное меню' if item.menu_type == 'main' else 'Банкетное меню'
        
        if menu_type_name not in result:
            result[menu_type_name] = {}
        
        if item.type_group_menu not in result[menu_type_name]:
            result[menu_type_name][item.type_group_menu] = []
        
        result[menu_type_name][item.type_group_menu].append({
            "id": item.id,
            "name": item.name,
            "description": item.description if item.description else None,
            "price": item.price,
            "gramms": item.gramms if item.gramms else None,
            "created_at": item.created_at,
            "updated_at": item.updated_at,
            "available_at_restaurant": item.available_at_restaurant,
            "type_group_menu": item.type_group_menu,
            "image_url": item.image_url.url if item.image_url else None,
            "what_cuisine_dish": item.what_cuisine_dish
        })
    
    return JsonResponse(result)

#получение основного меню
@api.get('/menu/main', tags=['Меню'])
def get_main_menu(request):
    menu_items = Menu.objects.filter(menu_type='main')  # type: ignore
    grouped = defaultdict(list)
    
    for item in menu_items:
        grouped[item.type_group_menu].append({
            "id": item.id,
            "name": item.name,
            "description": item.description if item.description else None,
            "price": item.price,
            "gramms": item.gramms if item.gramms else None,
            "created_at": item.created_at,
            "updated_at": item.updated_at,
            "available_at_restaurant": item.available_at_restaurant,
            "type_group_menu": item.type_group_menu,
            "image_url": item.image_url.url if item.image_url else None,
            "what_cuisine_dish": item.what_cuisine_dish
        })
    
    return JsonResponse(dict(grouped))

#получение банкетного меню
@api.get('/menu/banquet', tags=['Меню'])
def get_banquet_menu(request):
    menu_items = Menu.objects.filter(menu_type='banquet')  # type: ignore
    grouped = defaultdict(list)
    
    for item in menu_items:
        grouped[item.type_group_menu].append({
            "id": item.id,
            "name": item.name,
            "description": item.description if item.description else None,
            "price": item.price,
            "gramms": item.gramms if item.gramms else None,
            "created_at": item.created_at,
            "updated_at": item.updated_at,
            "available_at_restaurant": item.available_at_restaurant,
            "type_group_menu": item.type_group_menu,
            "image_url": item.image_url.url if item.image_url else None,
            "what_cuisine_dish": item.what_cuisine_dish
        })
    
    return JsonResponse(dict(grouped))

#получение блюда по id
@api.get('/menu/{menu_id}', response=MenuResponseSchema, tags=['Меню'])
def get_menu_item(request, menu_id: int):
    menu = Menu.objects.get(id=menu_id)  # type: ignore
    return menu

#обновление блюда
@api.put('/menu/{menu_id}', response=MenuResponseSchema, tags=['Меню'])
def update_menu(request, menu_id: int, menu: MenuSchema):
    data = menu.dict()
    menu_obj = Menu.objects.get(id=menu_id)  # type: ignore
    for key, value in data.items():
        setattr(menu_obj, key, value)
    menu_obj.save()
    return menu_obj

#загрузка изображения блюда
@api.post('/menu/{menu_id}/upload_image', tags=['Меню'])
def upload_menu_image(request, menu_id: int, image: UploadedFile):
    try:
        menu_obj = Menu.objects.get(id=menu_id)  # type: ignore
        menu_obj.image_url.save(image.name, image)
        menu_obj.save()
        return {"success": True, "image_url": menu_obj.image_url.url}
    except ObjectDoesNotExist:
        return {"success": False, "error": "Блюдо не найдено"}

#создание обратной связи
@api.post('/feedback', response=FeedbackResponseSchema, tags=['Обратная связь'])
def create_feedback(request, feedback: FeedbackSchema):
    data = feedback.dict()
    feedback_obj = Feedback.objects.create(**data)  # type: ignore
    return feedback_obj

#получение всех обращений
@api.get('/feedback', tags=['Обратная связь'])
def get_feedback(request):
    feedback = Feedback.objects.all()  # type: ignore
    return list(feedback)

#получение обращения по id
@api.get('/feedback/{feedback_id}', response=FeedbackResponseSchema, tags=['Обратная связь'])
def get_feedback_item(request, feedback_id: int):
    feedback = Feedback.objects.get(id=feedback_id)  # type: ignore
    return feedback

#urls для админки и api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

#для загрузки изображений и статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)