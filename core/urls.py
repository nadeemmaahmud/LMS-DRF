from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . views import CategoryViewSet, CourseViewSet, LessonViewSet, MetarialViewSet, EnrollmentViewSet, QuestionAnswerViewSet, AnswerViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('courses', CourseViewSet, basename='course')
router.register('lessons', LessonViewSet, basename='lesson')
router.register('metarials', MetarialViewSet, basename='metarial')
router.register('enrollments', EnrollmentViewSet, basename='enrollment')
router.register('questionanswers', QuestionAnswerViewSet, basename='questionanswer')
router.register('answers', AnswerViewSet, basename='answer')

urlpatterns = [
    path('', include(router.urls)),
]