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
        request.data['acara'] = acara_id
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SponsorUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Sponsor.objects.get(pk=pk)
        except Sponsor.DoesNotExist:
            return None

    def put(self, request, pk):
        sponsor = self.get_object(pk)
        serializer = SponsorSerializer(sponsor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        sponsor = self.get_object(pk)
        sponsor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PembicaraCreateReadAPIView(APIView):
    def get(self, request, acara_id):
        pembicaras = Pembicara.objects.filter(acara=acara_id)
        serializer = PembicaraSerializer(pembicaras, many=True)
        return Response(serializer.data)
    
    def post(self, request, acara_id):
        request.data['acara'] = acara_id  # Set the acara field based on the URL parameter
        serializer = PembicaraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PembicaraUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Pembicara.objects.get(pk=pk)
        except Pembicara.DoesNotExist:
            return None

    def put(self, request, pk):
        pembicara = self.get_object(pk)
        serializer = PembicaraSerializer(pembicara, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        pembicara = self.get_object(pk)
        pembicara.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PengurusIntiListCreateAPIView(APIView):
    def get(self, request):
        pengurusintis = PengurusInti.objects.all()
        serializer = PengurusIntiSerializer(pengurusintis, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PengurusIntiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PengurusIntiRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return PengurusInti.objects.get(pk=pk)
        except PengurusInti.DoesNotExist:
            return None

    def get(self, request, pk):
        pengurusinti = self.get_object(pk)
        serializer = PengurusIntiSerializer(pengurusinti)
        return Response(serializer.data)

    def put(self, request, pk):
        pengurusinti = self.get_object(pk)
        serializer = PengurusIntiSerializer(pengurusinti, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pengurusinti = self.get_object(pk)
        pengurusinti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DivisiListAPIView(APIView):
    def get(self, request):
        divisis = Divisi.objects.all()
        serializer = DivisiSerializer(divisis, many=True)
        return Response(serializer.data)

class DivisiCreateAPIView(APIView):
    def post(self, request):
        serializer = DivisiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RapatListCreateAPIView(APIView):
    def get(self, request, divisi_name):
        rapats = Rapat.objects.all().filter(divisi=divisi_name)
        serializer = RapatSerializer(rapats, many=True)
        return Response(serializer.data)

    def post(self, request, divisi_name):
        request.data["divisi"] = divisi_name
        serializer = RapatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RapatRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Rapat.objects.get(pk=pk)
        except Rapat.DoesNotExist:
            return None

    def get(self, request, pk):
        rapat = self.get_object(pk)
        serializer = RapatSerializer(rapat)
        return Response(serializer.data)

    def put(self, request, pk):
        rapat = self.get_object(pk)
        serializer = RapatSerializer(rapat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rapat = self.get_object(pk)
        rapat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BPHListCreateAPIView(APIView):
    def get(self, request, divisi_name):
        bphs = BPH.objects.all().filter(divisi=divisi_name)
        serializer = BPHSerializer(bphs, many=True)
        return Response(serializer.data)

    def post(self, request, divisi_name):
        request.data["divisi"] = divisi_name
        serializer = BPHSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BPHRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return BPH.objects.get(pk=pk)
        except BPH.DoesNotExist:
            return None

    def get(self, request, pk):
        bph = self.get_object(pk)
        serializer = BPHSerializer(bph)
        return Response(serializer.data)

    def put(self, request, pk):
        bph = self.get_object(pk)
        serializer = BPHSerializer(bph, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bph = self.get_object(pk)
        bph.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)