from django.urls import path
from . import views

app_name = 'admn'

urlpatterns = [
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    

    path('home',views.home,name='home'),
    path('teachers_page',views.teachers_page,name='teachers_page'),
    path('add_teacher',views.add_teacher,name='add_teacher'),
    path('view_teacher',views.view_teacher,name='view_teacher'),
    path('salary_page',views.salary_page,name='salary_page'),
    path('view_salary',views.view_salary,name='view_salary'),
    


    path('student_page',views.student_page,name='student_page'),
    path('view_student/<int:class_id>',views.view_student,name='view_student'),
    path('update_student',views.update_student,name='update_student'),


    path('fees_page',views.fees_page,name='fees_page'),
    path('view_feesdetails',views.view_feesdetails,name='view_feesdetails'),

    path('notification_page',views.notification_page,name='notification_page'),
    path('add_notification',views.add_notification,name='add_notification'),
    path('view_notification',views.view_notification,name='view_notification'),

    path('complaints_page',views.complaints_page,name='complaints_page'),


    path('update_salary/<int:teacher_id>',views.update_salary,name='update_salary'),
    path('edit_salary/<int:teach_id>',views.edit_salary,name='edit_salary'),

    path('attendance_class',views.attendance_class, name = 'attendance_class'),
    path('attendance_view/<int:classid>',views.attendance_view, name = 'attendance_view')
     






]