from django.urls import path
from . import views
app_name = 'common'
urlpatterns = [
    path('common_home',views.common_home,name='common_home'),
    path('parent_login',views.parent_login,name='parent_login'),
    path('teachers_login',views.teachers_login,name='teachers_login'),


]