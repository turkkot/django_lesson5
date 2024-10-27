from rest_framework import serializers
from studentWorksPlatform import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.IntegerField(required=False, allow_null=True)
    price = serializers.SerializerMethodField()
    class Meta:
        model = models.Work
        fields = '__all__'

    def get_price(self, obj):
        return obj.price