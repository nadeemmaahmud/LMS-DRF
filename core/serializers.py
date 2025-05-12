from rest_framework import serializers
from .models import Course, Lesson, Category, Metarials, Enrollment, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'banner', 'price', 'duration', 'category_id', 'instructor_id']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'course_id']

class MetarialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metarials
        fields = ['id', 'title', 'description', 'file_type', 'course_id']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'price', 'progress', 'total_mark', 'student_id', 'course_id']

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'description', 'lesson_id', 'student_id']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'user_id', 'answer']