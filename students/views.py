import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from students.models import Student

# Create your views here.
def student_home(request):
    return render(request, 'students/base.html')

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        Student.objects.create(id = body.get('id'), name = body.get('name'), age = body.get('age'), email = body.get('email'), city = body.get('city'))
        
    return JsonResponse({'message': 'Student Created Successfully'}, status=201)

def get_students(request):
    students =  Student.objects.all().values() 
    return JsonResponse({'message': 'Student List Retrieved', 'student_list': list(students)}, status=200)

@csrf_exempt
def update_Student(request, id):
    try:
        current_student = Student.objects.get(id = id)
        if request.method == 'PUT':
            body = json.loads(request.body)
            current_student.name = body.get('name')
            current_student.age = body.get('age')
            current_student.email = body.get('email')
            current_student.city = body.get('city')
            current_student.save()
            
            return JsonResponse({'message': 'Student updated successfully'}, status=200)
        else :
            return JsonResponse({'message': 'Student updated unsuccessfully'}, status=400)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'Student Does Not Exist!'}, status=404)
        

@csrf_exempt
def delete_student(request, id):
    try:
        current_student = Student.objects.get(id = id)
        if request.method == 'DELETE':
            current_student.delete()
            return JsonResponse({'message': 'Student deleted successfully'}, status=200)
        else :
            return JsonResponse({'message': 'Student deleted unsuccessfully'}, status=400)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'Student Does Not Exist!'}, status=404)
