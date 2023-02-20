from rest_framework import serializers
from django.utils.http import urlencode
from rest_framework.reverse import reverse as original_reverse
from quiz_app.models import (
    Subject,
    Question,
)
from rest_framework.pagination import PageNumberPagination

class QuestionPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1

def reverse(*args, **kwargs):
    print(args)
    print(kwargs)
    get = kwargs.pop('get', {})
    url = original_reverse(*args, **kwargs)

    if get:
        url += '?' + urlencode(get)

    return url

class SubjectPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_name','time_duration']

    def validate(self, attrs):

        get_subject_obj = Subject.objects.filter(subject_name__iexact=attrs.get('subject_name')).exists()
        if get_subject_obj:
            raise serializers.ValidationError({"subject_name":"This Subject is already Added"})
        return attrs

    def create(self, validated_data):

        subject_instance = Subject(
            subject_name=validated_data['subject_name'],
            time_duration=validated_data['time_duration']
        )
        subject_instance.save()
        return subject_instance


class SubjectDetailSerializer(serializers.ModelSerializer):
    number_of_questions = serializers.CharField()
    question_url= serializers.SerializerMethodField()
    class Meta:
        model = Subject
        fields = ['subject_name','number_of_questions','time_duration','question_url']

    def get_question_url(self,instance):
        get_subject_name = self.context.get("subject_name", None)
        return reverse('question-list',get={"subject_name":get_subject_name})

class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','subject_name']


class QuestionListSerializer(serializers.ModelSerializer):
    subject = SubjectListSerializer()   
    class Meta:
        model = Question
        fields = ['subject','id','question_name','op1','op2','op3','op4']
        

class QuestionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['subject','question_name','op1','op2','op3','op4','answer']

    def create(self, validated_data):
        question_instance = Question(
            subject=validated_data['subject'],
            question_name=validated_data['question_name'],
            op1=validated_data['op1'],
            op2=validated_data['op2'],
            op3=validated_data['op3'],
            op4=validated_data['op4'],
            answer=validated_data['answer']
        )
        question_instance.save()
        return question_instance