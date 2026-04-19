from django.urls import path

from teachers.views import TeacherDetailView, TeacherListCreatView


urlpatterns = [
    path('teachers/', TeacherListCreatView.as_view(), name='teacher-list-create'),
    path('teachers/<int:id>/', TeacherDetailView.as_view(), name='teacher-detail'),
]