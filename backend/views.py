from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .views import *
from .serializers import *

class AcaraAPIView(APIView):
    def post(self, request):
        serializer = AcaraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        all_acara = Acara.objects.all()
        serializer = AcaraSerializer(all_acara, many=True)
        return Response(serializer.data)
    
    # Only can be called manually
    def delete(self, request):
        Acara.objects.all().delete()
        return Response(status=status.HTTP_200_OK)
    
class SponsorCreateReadAPIView(APIView):
    def get(self, request, acara_id):
        sponsor = Sponsor.objects.all().filter(acara=acara_id)
        serializer = SponsorSerializer(sponsor, many=True)
        return Response(serializer.data)
    
    def post(self, request, acara_id):
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SponsorUpdateDeleteAPIView(APIView):
    def put(self, request, pk):
        sponsor = self.get_object(pk)
        serializer = SponsorSerializer(sponsor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        sponsor = self.get_object(pk)
        serializer = SponsorSerializer(sponsor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
