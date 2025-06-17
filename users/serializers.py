from rest_framework import serializers
from . models import CommuityMembers, Staff

class CommunityMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityMembers
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    model = Staff
    fields = '__all__'from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Users, Staff


#Built-in Django User serializer (for authentication and registration)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


#Serializer for creating/registering a new User along with Users profile
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)

    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'role', 'department', 'phone_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        user_profile = Users.objects.create(user=user, **validated_data)
        return user_profile


# Users profile serializer (view user profile info)
class UsersSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Users
        fields = ['user', 'role', 'department', 'phone_number']


# Staff model serializer
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
