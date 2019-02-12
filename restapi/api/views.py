from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from restapi.api.serializers import UserSerializer, GroupSerializer
from .models import Person
from .serializers import PersonSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ListPersonView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
