from rest_framework.response import Response
from rest_framework import status


def get_exception_context(exception):
    context={
        'status': status.HTTP_400_BAD_REQUEST,
        'success': False,
        'response': str(exception)
    }
    return Response(context, status=status.HTTP_400_BAD_REQUEST)


def get_serializer_context(serializer):
    context = {
            'status':status.HTTP_200_OK,
            'success':True,
            'response':serializer.data,
    }
    return Response(context,status=status.HTTP_200_OK)