from rest_framework import serializers
from routes.models import Route, RouteUser

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class RouteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteUser
        fields = '__all__'