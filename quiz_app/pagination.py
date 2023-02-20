from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

class Mypagination(PageNumberPagination):
    page_size = 1

    def get_paginated_response(self, data):
        get_subject_name = self.request.query_params.get('subject_name')
        if get_subject_name:
            context ={
                'status':status.HTTP_200_OK,
                'success':True,
                'response':data,
                'links': {'next': self.get_next_link(),'previous': self.get_previous_link()}
            }
            return Response(context,status=status.HTTP_200_OK)

        else:
            context = {
            'status': status.HTTP_400_BAD_REQUEST,
            'success':False,
            'response':"Subject name must be passed"
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)