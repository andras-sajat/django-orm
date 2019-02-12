from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def askme(request):
    """
    Say hello
    """
    if request.method == 'GET':
        return Response("Hello")
