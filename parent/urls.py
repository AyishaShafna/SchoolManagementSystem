from django.urls import path
from . import views
app_name = 'parent'
urlpatterns = [
    
    path('parent_home',views.parent_home,name='parent_home'),
    path('stdnt_dtls/<int:sid>',views.stdnt_dtls,name='stdnt_dtls'),
    path('view_attendance/<int:sid>',views.view_attendance,name='view_attendance'),
    path('parent_logout',views.parent_logout, name = 'parent_logout')




]