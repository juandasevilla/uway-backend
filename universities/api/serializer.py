from rest_framework import serializers
from universities.models import University, UniversityColors


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class UniversityColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityColors
        fields = '__all__'