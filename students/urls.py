from django.urls import path
from students import views

urlpatterns = [
    path('', views.student_home, name='student_home'),
    path('add_students/', views.add_student, name='add_students'),
    path('get_students/', views.get_students, name='get_students'),
    path('update_students/<int:id>', views.update_Student, name='update_students'),
    path('delete_students/<int:id>', views.delete_student, name='delete_students'),
]