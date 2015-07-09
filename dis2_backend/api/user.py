import dis2_backend.serializers as sr
from dis2_backend.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class UserList(APIView):
    def get(self, request, format=None):
        users = AppUser.objects.all()
        serializer = sr.AppUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = sr.AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return AppUser.objects.get(pk=pk)
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = sr.AppUserSerializer(user)
        return Response(serializer.data)

class UserSchoolsList(APIView):
    def get_objects(self, pk):
        try:
            return AppUser.objects.get(pk=pk).schools.all()
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.SchoolSerializer(objects, many=True)
        return Response(serializer.data)

class UserGroupsList(APIView):
    def get_objects(self, pk):
        try:
            return AppUser.objects.get(pk=pk).groups.all()
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.GroupSerializer(objects, many=True)
        return Response(serializer.data)

class UserEventsList(APIView):
    def get_objects(self, pk):
        try:
            return AppUser.objects.get(pk=pk).events.all()
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.EventSerializer(objects, many=True)
        total = 0
        for item in serializer.data:
            total += item['value']
        return Response({'total': total,
                         'events': serializer.data})

class UserAchievementList(APIView):
    def get_objects(self, pk):
        try:
            return AppUser.objects.get(pk=pk).achievements.all()
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.AchievementSerializer(objects, many=True)
        return Response(serializer.data)
