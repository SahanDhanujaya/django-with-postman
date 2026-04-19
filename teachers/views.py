from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer

# Create your views here.

# api/teachers/
class TeacherListCreatView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# api/teachers/<int:id>
class TeacherDetailView(APIView):
    def get_object(self, id):
        try:
            return Teacher.objects.get(id=id)
        except Teacher.DoesNotExist:
            return None
        
    def put(self, request, id):
        current_teacher = self.get_object(id)
        if not current_teacher:
            return Response({"error": "Teacher Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(current_teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        current_teacher = self.get_object(id)
        if not current_teacher:
            return Response({"error": "Teacher Not Found"}, status=status.HTTP_404_NOT_FOUND)
        current_teacher.delete()
        return Response({"message": "TEacher Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        
        