from django.shortcuts import render
from .models import Students
from .serilize import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_detil(request):
    res = Students.objects.all()
    serializer = StudentSerilizer(res, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
