from rest_framework import serializers
from .models import *

class AcaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acara
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class PembicaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembicara
        fields = '__all__'

class PengurusIntiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PengurusInti
        fields = '__all__'

class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = '__all__'

class RapatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapat
        fields = '__all__'

class BPHSerializer(serializers.ModelSerializer):
    class Meta:
        model = BPH
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class KelompokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kelompok
        fields = '__all__'

class MenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentee
        fields = '__all__'

class MentoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentoring
        fields = '__all__'
