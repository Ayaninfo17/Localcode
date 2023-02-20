from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    time_duration = models.CharField(max_length=100,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Subject"


    def __str__(self):
        return "{}".format(self.subject_name)


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name="subject_question")
    question_name = models.CharField(max_length=200)
    op1 = models.CharField(_('option1'),max_length=100,blank=True)
    op2 = models.CharField(_('option2'),max_length=100,blank=True)
    op3 = models.CharField(_('option3'),max_length=100,blank=True)
    op4 = models.CharField(_('option4'),max_length=100,blank=True)
    answer = models.CharField(_('answer'),max_length=100,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Question"


    def __str__(self):
        return "{}".format(self.question_name)
