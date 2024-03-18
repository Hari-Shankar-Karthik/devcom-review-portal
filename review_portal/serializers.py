from rest_framework import serializers
from .models import Course
from .models import Department

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "department", "code", "name", "info", "review", "ratings", "average_rating"]
        # Excluding department from POST request
        extra_kwargs = {'department': {'required': False}}

class DepartmentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ["id", "name", "courses"]
