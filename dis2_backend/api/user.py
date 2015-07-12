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

    def post(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = sr.AppUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class UserAddSchool(APIView):
    def get_object(self, model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        user = self.get_object(AppUser, pk)
        school = self.get_object(School, request.data['school'])
        user.schools.add(school)
        user.save()

        return Response(status=status.HTTP_200_OK)

class UserRemoveSchool(APIView):
    def get_object(self, model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        user = self.get_object(AppUser, pk)
        school = self.get_object(School, request.data['school'])
        user.schools.remove(school)
        user.save()

        return Response(status=status.HTTP_200_OK)

class UserAddGroup(APIView):
    def get_object(self, model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        user = self.get_object(AppUser, pk)
        group = self.get_object(Group, request.data['group'])
        user.groups.add(group)
        user.save()

        return Response(status=status.HTTP_200_OK)

class UserRemoveGroup(APIView):
    def get_object(self, model, pk):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        user = self.get_object(AppUser, pk)
        group = self.get_object(Group, request.data['group'])
        user.groups.remove(group)
        user.save()

        return Response(status=status.HTTP_200_OK)

