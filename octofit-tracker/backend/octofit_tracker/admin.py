from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team_id', 'created_at')
    list_filter = ('created_at', 'team_id')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'user_id', 'duration', 'calories_burned', 'date', 'created_at')
    list_filter = ('activity_type', 'date', 'created_at')
    search_fields = ('user_id', 'activity_type', 'notes')
    ordering = ('-created_at',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('rank', 'user_id', 'team_id', 'total_calories', 'total_duration', 'updated_at')
    list_filter = ('rank', 'updated_at')
    search_fields = ('user_id', 'team_id')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_type', 'difficulty', 'duration', 'calories_estimate', 'created_at')
    list_filter = ('difficulty', 'activity_type', 'created_at')
    search_fields = ('name', 'description', 'activity_type')
    ordering = ('-created_at',)
