from django.urls import path

from teachers.views import TeacherDetailView, TeacherListCreateView


urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:id>/', TeacherDetailView.as_view(), name='teacher-detail'),
]