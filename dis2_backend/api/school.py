import dis2_backend.serializers as sr
from dis2_backend.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class SchoolList(APIView):
    def get(self, request, format=None):
        schools = School.objects.all()
        serializer = sr.SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = sr.SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolDetail(APIView):
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        school = self.get_object(pk)
        serializer = sr.SchoolSerializer(school)
        return Response(serializer.data)

class SchoolStudentsList(APIView):
    def get_objects(self, pk):
        try:
            return School.objects.get(pk=pk).members.filter(user__is_staff=False)
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.AppUserSerializer(objects, many=True)
        return Response(serializer.data)

class SchoolStaffList(APIView):
    def get_objects(self, pk):
        try:
            return School.objects.get(pk=pk).members.filter(user__is_staff=True)
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.AppUserSerializer(objects, many=True)
        return Response(serializer.data)

class SchoolGroupsList(APIView):
    def get_objects(self, pk):
        try:
            return School.objects.get(pk=pk).groups.all()
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.GroupSerializer(objects, many=True)
        return Response(serializer.data)

class SchoolRewardsList(APIView):
    def get_objects(self, pk):
        try:
            return School.objects.get(pk=pk).rewards.all()
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.RewardSerializer(objects, many=True)
        return Response(serializer.data)

class SchoolEventsList(APIView):
    def get_objects(self, pk):
        try:
            return School.objects.get(pk=pk).events.all()
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
