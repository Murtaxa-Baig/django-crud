from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Students
from .serilize import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.
def student_detail(request):
    students = Students.objects.all()
    serializer = StudentSerilizer(students, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def student_api(request):
    if request.method == "GET":
        student_id = request.GET.get('id', None)

        if student_id is not None:
            student = get_object_or_404(Students, id=student_id)
            serializer = StudentSerilizer(student)
            return JsonResponse(serializer.data, safe=False)

        students = Students.objects.all()
        serializer = StudentSerilizer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)
