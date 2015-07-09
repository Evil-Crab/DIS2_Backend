from rest_framework import serializers
from dis2_backend.models import *

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class AppUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    is_staff = serializers.CharField(source='user.is_staff')
    email = serializers.CharField(source='user.email')
    avatar = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'is_staff', 'email', 'avatar', 'bio')
        extra_kwargs = {'password': {'write_only': True}}

    def get_validation_exclusions(self):
        exclusions = super(AppUserSerializer, self).get_validation_exclusions()
        return exclusions + ['avatar', 'bio']

    def create(self, validated_data):
        validated_data['user'] = User.objects.create(**validated_data['user'])
        validated_data['user'].set_password(str(validated_data.pop('password')))
        validated_data['user'].save()
        appUser = AppUser.objects.create(**validated_data)

        return appUser

class SchoolSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False)
    sigil = serializers.ImageField(required=False)

    class Meta:
        model = School
        fields = ('id', 'name', 'description', 'sigil', )

    def get_validation_exclusions(self):
        exclusions = super(SchoolSerializer, self).get_validation_exclusions()
        return exclusions + ['description', 'sigil']

class GroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    color = serializers.CharField(max_length=7)
    sigil = serializers.ImageField(required=False)

    class Meta:
        model = Group
        fields = ('id', 'name', 'color', 'sigil', )

    def get_validation_exclusions(self):
        exclusions = super(GroupSerializer, self).get_validation_exclusions()
        return exclusions + ['sigil']

class RewardSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False)
    requirements = serializers.CharField(required=False)

    class Meta:
        model = Reward
        fields = ('id', 'name', 'description', 'requirements', )

    def get_validation_exclusions(self):
        exclusions = super(RewardSerializer, self).get_validation_exclusions()
        return exclusions + ['description', 'requirements', ]

class EventSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(default=0)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False)

    school = serializers.PrimaryKeyRelatedField(read_only=True)
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'value', 'name', 'description', 'school', 'students')

    def get_validation_exclusions(self):
        exclusions = super(EventSerializer, self).get_validation_exclusions()
        return exclusions + ['description']

class AchievementSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False)
    requirements = serializers.CharField(required=False)
    badge = serializers.ImageField(required=False)

    class Meta:
        model = Achievement
        fields = ('id', 'name', 'description', 'requirements', 'badge')

    def get_validation_exclusions(self):
        exclusions = super(AchievementSerializer, self).get_validation_exclusions()
        return exclusions + ['description', 'requirements', 'badge']
