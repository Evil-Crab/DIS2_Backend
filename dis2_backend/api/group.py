import dis2_backend.serializers as sr
from dis2_backend.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class GroupList(APIView):
    def get(self, request, format=None):
        users = Group.objects.all()
        serializer = sr.GroupSerializer(users, many=True)
        return Response(serializer.data)

class GroupDetail(APIView):
    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = sr.GroupSerializer(group)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = sr.GroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupStudentsList(APIView):
    def get_objects(self, pk):
        try:
            return Group.objects.get(pk=pk).members.all()
        except AppUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objects = self.get_objects(pk)
        serializer = sr.AppUserSerializer(objects, many=True)
        return Response(serializer.data)

class GroupEventsList(APIView):
    def get_objects(self, pk):
        try:
            students = Group.objects.get(pk=pk).members.all()
            events = Event.objects.none()
            for student in students:
                events = events | student.events.all()

            return events
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
