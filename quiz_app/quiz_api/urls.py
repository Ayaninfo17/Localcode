from django.urls import path
from quiz_app.quiz_api.views import (
    SubjectPostAPI,
    QuestionPostAPI,
    SubjectDetailView,
    SubjectListView,
    CorrectAnswerView,
    QuestioinList
    
)

urlpatterns = [

    path('post-subject/',SubjectPostAPI.as_view(),name='post-subject'),
    path('post-question/',QuestionPostAPI.as_view(),name='post-question'),
    path('subject-list/',SubjectListView.as_view(),name='subject-list'),
    path('subject-detail/',SubjectDetailView.as_view(),name='subject-detail'),
    path('correct-answer/',CorrectAnswerView.as_view(),name='correct-answer'),
    path('question-list/',QuestioinList.as_view(),name='question-list'),


    
]
