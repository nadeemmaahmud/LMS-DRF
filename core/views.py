from django.shortcuts import render
from rest_framework import viewsets, permissions

from . models import Course, Lesson, Question, Category, Enrollment, Metarials, Answer
from . serializers import CourseSerializer, LessonSerializer, QuestionAnswerSerializer, CategorySerializer, EnrollmentSerializer, MetarialSerializer, AnswerSerializer
from . permissions import IsTeacher, IsStudent

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsTeacher]

class MetarialViewSet(viewsets.ModelViewSet):
    queryset = Metarials.objects.all()
    serializer_class = MetarialSerializer
    permission_classes = [IsTeacher]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsStudent]
    
class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionAnswerSerializer
    permission_classes = [IsStudent]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsTeacher]