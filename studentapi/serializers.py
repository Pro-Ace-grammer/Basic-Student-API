from rest_framework import serializers
from .models import Student

# Create your serializers here

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     rollno = serializers.IntegerField()
#     course = serializers.CharField()

#     def create(self, validated_data):
#         stu = Student.objects.create(**validated_data)
#         return 
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.rollno = validated_data.get('rollno', instance.rollno)
#         instance.course = validated_data.get('course', instance.course)
#         instance.save()
#         return instance