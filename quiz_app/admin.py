from django.contrib import admin
from quiz_app.models import (
    Subject,
    Question,
)

# Register your models here.

admin.site.register(Subject)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['subject','question_name']

admin.site.register(Question,QuestionAdmin)
