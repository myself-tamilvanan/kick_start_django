from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Students

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ["url", "username", "email", "groups"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ["url", "name"]
    
class StudentSerializer(serializers.ModelSerializer):
  first_name = serializers.CharField(max_length=200, required=True)
  last_name = serializers.CharField(max_length=200, required=True)
  address = serializers.CharField(max_length=200, required=True)
  roll_no = serializers.IntegerField()
  mobile_no = serializers.CharField(max_length=10, required=True)
  
  def create(self, validated_data):
    return Students.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    instance.first_name = validated_data.get("first_name", instance.first_name)
    instance.last_name = validated_data.get("last_name", instance.last_name)
    instance.address = validated_data.get("address", instance.address)
    instance.roll_number = validated_data.get("roll_number", instance.roll_number)
    instance.mobile = validated_data.get("mobile", instance.mobile)
    instance.save()
    
    return instance
    
    
  class Meta:
    model = Students
    fields = "__all__"