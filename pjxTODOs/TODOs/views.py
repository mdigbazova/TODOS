from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics

from . models import Profile
from . serializers import UserCreateSerializer, ProfileSerializer
from . permissions import IsOwnerOrReadOnly
from .method_serializer_view import MethodSerializerView

# Create your views here.


# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()


#------------------------


class RegisterUser(MethodSerializerView, generics.ListCreateAPIView):
    permissions_classes = [permissions.AllowAny, ]

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    method_serializer_classes = {
        ('POST'): UserCreateSerializer
    }

#------------------------

class UserList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        #'register_user': reverse('register', request=request, format=format),
        'alerts_bodies': reverse('alerts-bodies', request=request, format=format),
        'accounts': reverse('accounts', request=request, format=format),
        'agents': reverse('agents', request=request, format=format),
        'comments': reverse('comments', request=request, format=format),

    })

#--------------------------

#--------------------------
