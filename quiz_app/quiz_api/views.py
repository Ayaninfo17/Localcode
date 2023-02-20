import json
from operator import itemgetter
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from quiz_app.pagination import Mypagination
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from django.shortcuts import (
    get_object_or_404,
    get_list_or_404,
)
from django.db.models import (
    OuterRef,
    Count,
    Value,
    F,
)
from quiz_app.models import (
    Subject,
    Question,
)
from rest_framework.pagination import PageNumberPagination

from quiz_app.quiz_api.serializer import (
    SubjectDetailSerializer,
    SubjectListSerializer,
    SubjectPostSerializer,
    QuestionPostSerializer,
    QuestionPagination,
    QuestionListSerializer
)
from quiz_app.helpers import (
    get_serializer_context,
    get_exception_context,
    
)

class SubjectListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_subject_list = Subject.objects.all().order_by('-id')
            serializer = SubjectListSerializer(get_subject_list,many=True)
            return get_serializer_context(serializer)

        except Exception as exception:
            return get_exception_context(exception)


class SubjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_subject_name = self.request.query_params.get('subject_name')
            if get_subject_name:

                get_subject_list = Subject.objects.filter(subject_name__iexact=get_subject_name
                    ).annotate(
                        number_of_questions = Question.objects.filter(subject_id=OuterRef("id")
                                                    ).values("subject_id"
                                                        ).annotate(number_of_questions=Count("id")).values("number_of_questions")
                        )

                serializer = SubjectDetailSerializer(get_subject_list,many=True,context = {"subject_name":get_subject_name})
                return get_serializer_context(serializer)

            else:
                context = {
                'status': status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':"Subject name must be passed"
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception:
            return get_exception_context(exception)


class SubjectPostAPI(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [BasicAuthentication]

    def post(self,request):
        try:
            data = request.data
            serializer = SubjectPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return get_serializer_context(serializer)
            
            else:
                serializer_error = serializer.errors
                serializer_error = {key: value[0] for key,value in serializer_error.items()}
                context = {
                    'status':status.HTTP_400_BAD_REQUEST,
                    'success':False,
                    'response':serializer_error,
                }
                return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception:
            return get_exception_context(exception)


class QuestionPostAPI(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes= [BasicAuthentication]
    def post(self, request):
        try:
            data = request.data
            serializer = QuestionPostSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return get_serializer_context(serializer)

            else:
                serializer_error = serializer.errors
                serializer_error = {key: value[0] for key,value in serializer_error.items()},
                context = {
                        'status':status.HTTP_400_BAD_REQUEST,
                        'success':False,
                        'response':serializer_error,
                }
                return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception:
            return get_exception_context(exception)


class QuestioinList(ListAPIView):
    serializer_class = QuestionListSerializer
    pagination_class = Mypagination

    def get_queryset(self):
        try:
            get_subject_name= self.request.query_params.get('subject_name')
            get_subject_question_obj = Question.objects.filter(
                                                subject__subject_name__iexact=get_subject_name
                                                                    ).select_related(
                                                                        'subject'
                                                                        ).order_by("-id")
            return get_subject_question_obj
        
        except Exception as exception:
            return get_exception_context(exception)


class CorrectAnswerView(APIView):
    def post(self, request,*args, **kwargs):
        try:
            get_json = request.POST.get('get_json',None)
            get_json_obj = json.loads(get_json)
            
            correct_count = 0
            wrong_count = 0
            
            for i in get_json_obj:
                question_obj = Question.objects.filter(id=i['id'], answer__iexact=i['op'])
                
                if question_obj:
                    correct_count += 1
                else:
                    wrong_count +=1
            
            context = {
                'status': status.HTTP_200_OK,
                'success':True,
                'response':{
                        "correct_answer":correct_count,
                        "wrong_answer":wrong_count
                        }
            }
            return Response(context,status=status.HTTP_200_OK)

        except Exception as exception:
            return get_exception_context(exception)
        