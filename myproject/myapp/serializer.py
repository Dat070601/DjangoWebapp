from rest_framework.serializers import ModelSerializer
from .models import Course
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","subject","image","create_date","category"] #Chi dinh cac truong can thiet de tham chieu 

