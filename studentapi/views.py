from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json

# Create your views here.
# all_students = [
#     {'id':1,'name':'Teja','rollno':34,'course':'Django'},
#     {'id':2,'name':'Naveena','rollno':23,'course':'Data Science'},
#     {'id':3,'name':'Mohammed','rollno':12,'course':'Django'},
# ]


# @csrf_exempt

@api_view(['POST','GET'])
def all_students_view(request):
    if request.method == 'POST':
        json_data = request.body
        py_data = json.loads(json_data)
        deserial = StudentSerializer(data=py_data)
        if deserial.is_valid():
            deserial.save()
            return Response({'msg':'Student Created Successfully'}, status=status.HTTP_201_CREATED)
        return Response({'msg':'Something Went Wrong!!'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        all_students = Student.objects.all()
        serial = StudentSerializer(all_students,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)




# @csrf_exempt

@api_view(['GET','PUT','DELETE'])
def get_edit_or_delete_student(request,id):
    try:
        stu = Student.objects.get(id=id) # {'name': 'Mohammed', 'rollno': 8, 'course': 'Django'}
    except:
        return Response({'msg':'404:Student Not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        json_data = request.body
        py_data = json.loads(json_data) # {'rollno': 13, 'course': 'Data Science'}
        deserial = StudentSerializer(stu, data=py_data, partial=True)
        print(deserial.is_valid())
        if deserial.is_valid():
            deserial.save()
            return Response({'msg':'Student Data Updated Successfully'},status=status.HTTP_200_OK)
        return Response({'msg':'Something Went Wrong!!'}, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'DELETE':
        stu.delete()
        return Response({'msg':'Student deleted Successfully!!'}, status=status.HTTP_204_NO_CONTENT)
    

    if request.method == 'GET':
        serial = StudentSerializer(stu)
        return Response(serial.data, status=status.HTTP_200_OK)






'''
Response:

'''




# def student_view(request,id):
#     data = None
#     # for student in all_students:
#     #     if student['id'] == id:
#     #         data = student
#     #         break
#     # else:
#     #     error = {'error':'404: Student Not Found'}
#     #     json_data = json.dumps(error)
#     #     return HttpResponse(json_data)
    
#     json_data = json.dumps(data)
#     return HttpResponse(json_data)

'''
Notes
LMS
Social Media ... 
E-Commerce 
'''

