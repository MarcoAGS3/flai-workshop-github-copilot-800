from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
    
    def __str__(self):
        return f"{self.activity_type} - {self.duration} mins"


class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100)
    total_calories = models.IntegerField()
    total_duration = models.IntegerField()  # in minutes
    rank = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
    
    def __str__(self):
        return f"Rank {self.rank} - {self.total_calories} calories"


class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    duration = models.IntegerField()  # in minutes
    calories_estimate = models.IntegerField()
    activity_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.name
