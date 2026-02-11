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
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at', 'member_count']
    
    def get_member_count(self, obj):
        """Get the count of users in this team"""
        try:
            team_id_str = str(obj._id)
            count = User.objects.filter(team_id=team_id_str).count()
            return count
        except Exception as e:
            return 0


class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'user_name', 'activity_type', 'duration', 'distance', 'calories_burned', 'date', 'notes', 'created_at']
    
    def get_user_name(self, obj):
        """Get the user's name from the user_id"""
        try:
            from bson import ObjectId as BsonObjectId
            # Try to get the user by converting the string _id to ObjectId
            user = User.objects.get(_id=BsonObjectId(obj.user_id))
            return user.name
        except (User.DoesNotExist, Exception) as e:
            # Fallback to a simple user ID display
            return f"User {obj.user_id}"


class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user_name = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    total_activities = serializers.SerializerMethodField()
    total_points = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'user_name', 'team_id', 'team_name', 'total_calories', 'total_points', 'total_duration', 'total_activities', 'rank', 'updated_at']
    
    def get_user_name(self, obj):
        """Get the user's name from the user_id"""
        try:
            from bson import ObjectId as BsonObjectId
            user = User.objects.get(_id=BsonObjectId(obj.user_id))
            return user.name
        except (User.DoesNotExist, Exception):
            return "Unknown User"
    
    def get_team_name(self, obj):
        """Get the team's name from the team_id"""
        try:
            from bson import ObjectId as BsonObjectId
            team = Team.objects.get(_id=BsonObjectId(obj.team_id))
            return team.name
        except (Team.DoesNotExist, Exception):
            return "N/A"
    
    def get_total_activities(self, obj):
        """Get the count of activities for this user"""
        try:
            count = Activity.objects.filter(user_id=obj.user_id).count()
            return count
        except Exception:
            return 0
    
    def get_total_points(self, obj):
        """Return total_calories as total_points for display purposes"""
        return obj.total_calories


class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'difficulty', 'duration', 'calories_estimate', 'activity_type', 'created_at']
