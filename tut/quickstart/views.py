#global imports
from django.contrib.auth.models import Group, User
from rest_framework import permissions , viewsets
#local imports 
from tut.quickstart.serializers import GroupSerializer , UserSerializer

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
class GroupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
