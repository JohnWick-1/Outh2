from django.contrib.auth.models import User, Group
from django.contrib import admin

# admin.autodiscover()

from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'




# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', "first_name", "last_name")
#

















'''

class ActivitySerializer(serializers.Serializer):
    pk= serializers.ReadOnlyField()
    name = serializers.CharField(max_length=55)
    description = serializers.CharField(required=False)

    def restore_object(self,attrs,instance):
        if instance:
            # update existing instance
            instance.name=attrs.get('name',instance.name)
            instance.description = attrs.get('description',instance.description)
            return instance

        #create new instance
        return Activity(**attrs)
'''

