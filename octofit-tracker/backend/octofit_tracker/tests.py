from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            password="password123"
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
    
    def test_user_str(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
    
    def test_team_str(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id="test_user_id",
            activity_type="Running",
            duration=30,
            calories_burned=300,
            date=date.today()
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories_burned, 300)
    
    def test_activity_str(self):
        """Test the string representation of an activity"""
        self.assertEqual(str(self.activity), "Running - 30 mins")


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_id="test_user_id",
            team_id="test_team_id",
            total_calories=1500,
            total_duration=150,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.leaderboard.total_calories, 1500)
        self.assertEqual(self.leaderboard.total_duration, 150)
        self.assertEqual(self.leaderboard.rank, 1)
    
    def test_leaderboard_str(self):
        """Test the string representation of a leaderboard entry"""
        self.assertEqual(str(self.leaderboard), "Rank 1 - 1500 calories")


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A refreshing morning run",
            difficulty="Medium",
            duration=45,
            calories_estimate=450,
            activity_type="Running"
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.difficulty, "Medium")
        self.assertEqual(self.workout.duration, 45)
    
    def test_workout_str(self):
        """Test the string representation of a workout"""
        self.assertEqual(str(self.workout), "Morning Run")


class UserAPITest(APITestCase):
    def test_create_user(self):
        """Test creating a user via API"""
        url = '/api/users/'
        data = {
            'name': 'API Test User',
            'email': 'apitest@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API Test User')


class TeamAPITest(APITestCase):
    def test_create_team(self):
        """Test creating a team via API"""
        url = '/api/teams/'
        data = {
            'name': 'API Test Team',
            'description': 'Team created via API'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'API Test Team')


class ActivityAPITest(APITestCase):
    def test_create_activity(self):
        """Test creating an activity via API"""
        url = '/api/activities/'
        data = {
            'user_id': 'test_user_id',
            'activity_type': 'Cycling',
            'duration': 60,
            'calories_burned': 500,
            'date': str(date.today())
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(Activity.objects.get().activity_type, 'Cycling')


class LeaderboardAPITest(APITestCase):
    def test_create_leaderboard_entry(self):
        """Test creating a leaderboard entry via API"""
        url = '/api/leaderboard/'
        data = {
            'user_id': 'test_user_id',
            'team_id': 'test_team_id',
            'total_calories': 2000,
            'total_duration': 200,
            'rank': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(Leaderboard.objects.get().total_calories, 2000)


class WorkoutAPITest(APITestCase):
    def test_create_workout(self):
        """Test creating a workout via API"""
        url = '/api/workouts/'
        data = {
            'name': 'Evening Yoga',
            'description': 'Relaxing yoga session',
            'difficulty': 'Easy',
            'duration': 30,
            'calories_estimate': 150,
            'activity_type': 'Yoga'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(Workout.objects.get().name, 'Evening Yoga')


class APIRootTest(APITestCase):
    def test_api_root(self):
        """Test that the API root endpoint returns all available endpoints"""
        url = '/api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
