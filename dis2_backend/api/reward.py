import dis2_backend.serializers as sr
from dis2_backend.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class CreateReward(APIView):
    def post(self, request, format=None):
        serializer = sr.RewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModifyReward(APIView):
    def get_object(self, pk):
        try:
            return Reward.objects.get(pk=pk)
        except Reward.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        reward = self.get_object(pk)
        serializer = sr.RewardSerializer(reward, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteReward(APIView):
    def get_object(self, pk):
        try:
            return Reward.objects.get(pk=pk)
        except Reward.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        reward = self.get_object(pk)
        reward.delete()

        return Response(status=status.HTTP_200_OK)

