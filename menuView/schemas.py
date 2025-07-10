from menuView.models import Menu
from feedback.models import Feedback
from ninja import ModelSchema

class MenuSchema(ModelSchema):
    class Config:
        model = Menu
        model_fields = ['name', 'gramms', 'description', 'price', 'menu_type', 'available_at_restaurant', 'type_group_menu', 'image_url', 'what_cuisine_dish']

class MenuResponseSchema(ModelSchema):
    class Config:
        model = Menu
        model_fields = ['id', 'name', 'gramms', 'description', 'price', 'created_at', 'updated_at', 'menu_type', 'available_at_restaurant', 'type_group_menu', 'image_url', 'what_cuisine_dish']

class FeedbackSchema(ModelSchema):
    class Config:
        model = Feedback
        model_fields = ['name', 'email', 'phone', 'subject', 'message']

class FeedbackResponseSchema(ModelSchema):
    class Config:
        model = Feedback
        model_fields = ['id', 'name', 'email', 'phone', 'subject', 'message', 'created_at']