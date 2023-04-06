from django.urls import path
from . import views
app_name = 'teacher'
urlpatterns = [
    path('teacher_home',views.teacher_home,name='teacher_home'),
    path('teacher_profile',views.teacher_profile,name='teacher_profile'),
    path('change_password',views.change_password,name='change_password'),
    path('teacher_logout',views.teacher_logout,name='teacher_logout'),

    path('add_students',views.add_students,name='add_students'),
    path('update_student',views.update_student,name='add_student'),
    path('view_student',views.view_student,name='view_student'),
    path('student_details/<int:student_id>',views.student_details,name='student_details'),
    path('update_student/<int:stdnt_id>',views.update_student,name='update_student'),

    
    path('add_result',views.add_result,name='add_result'),
    path('view_result',views.view_result,name='view_result'),
    path('update_result/<int:student_id>',views.update_result,name='update_result'),

   
    path('take_attendance',views.take_attendance,name='take_attendance'),
    path('view_attendance',views.view_attendance,name='view_attendance'),



    
]