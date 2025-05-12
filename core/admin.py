from django.contrib import admin
from .models import Course, Lesson, Category, Metarials, Enrollment, Question, Answer

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Metarials)
admin.site.register(Enrollment)
admin.site.register(Question)
admin.site.register(Answer)