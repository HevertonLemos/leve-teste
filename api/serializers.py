from rest_framework import serializers
from api.models import User, Salaries


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = "__all__"
