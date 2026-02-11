from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId


class ObjectIdField(serializers.Field):
    """Custom field to handle ObjectId serialization"""
    def to_representation(self, value):
        return str(value)
    
    def to_internal_value(self, data):
        return ObjectId(data)


class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'password', 'team_id', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}


class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'activity_type', 'duration', 'calories_burned', 'date', 'notes', 'created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'team_id', 'total_calories', 'total_duration', 'rank', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'difficulty', 'duration', 'calories_estimate', 'activity_type', 'created_at']
