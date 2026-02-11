from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta
from bson import ObjectId


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting existing data...'))
        
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data deleted'))
        
        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Mightiest heroes of Earth'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='World\'s greatest superheroes'
        )
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name} and {team_dc.name}'))
        
        # Create users (superheroes)
        self.stdout.write('Creating users...')
        
        # Team Marvel heroes
        iron_man = User.objects.create(
            name='Tony Stark',
            email='ironman@marvel.com',
            password='stark123',
            team_id=str(team_marvel._id)
        )
        captain_america = User.objects.create(
            name='Steve Rogers',
            email='cap@marvel.com',
            password='shield123',
            team_id=str(team_marvel._id)
        )
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@marvel.com',
            password='asgard123',
            team_id=str(team_marvel._id)
        )
        black_widow = User.objects.create(
            name='Natasha Romanoff',
            email='blackwidow@marvel.com',
            password='widow123',
            team_id=str(team_marvel._id)
        )
        hulk = User.objects.create(
            name='Bruce Banner',
            email='hulk@marvel.com',
            password='smash123',
            team_id=str(team_marvel._id)
        )
        
        # Team DC heroes
        superman = User.objects.create(
            name='Clark Kent',
            email='superman@dc.com',
            password='krypton123',
            team_id=str(team_dc._id)
        )
        batman = User.objects.create(
            name='Bruce Wayne',
            email='batman@dc.com',
            password='gotham123',
            team_id=str(team_dc._id)
        )
        wonder_woman = User.objects.create(
            name='Diana Prince',
            email='wonderwoman@dc.com',
            password='themyscira123',
            team_id=str(team_dc._id)
        )
        flash = User.objects.create(
            name='Barry Allen',
            email='flash@dc.com',
            password='speedforce123',
            team_id=str(team_dc._id)
        )
        aquaman = User.objects.create(
            name='Arthur Curry',
            email='aquaman@dc.com',
            password='atlantis123',
            team_id=str(team_dc._id)
        )
        
        marvel_heroes = [iron_man, captain_america, thor, black_widow, hulk]
        dc_heroes = [superman, batman, wonder_woman, flash, aquaman]
        all_heroes = marvel_heroes + dc_heroes
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_heroes)} users'))
        
        # Create activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Boxing', 'Yoga', 'CrossFit']
        activity_count = 0
        
        for i, hero in enumerate(all_heroes):
            # Each hero gets 3-5 activities
            num_activities = 3 + (i % 3)
            for j in range(num_activities):
                activity_type = activity_types[j % len(activity_types)]
                duration = 30 + (j * 15) + (i * 5)
                calories = duration * 8 + (i * 20)
                days_ago = j + (i * 2)
                
                Activity.objects.create(
                    user_id=str(hero._id),
                    activity_type=activity_type,
                    duration=duration,
                    calories_burned=calories,
                    date=date.today() - timedelta(days=days_ago),
                    notes=f'{hero.name} crushing {activity_type}!'
                )
                activity_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activity_count} activities'))
        
        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Super Soldier Circuit',
                'description': 'High-intensity circuit training worthy of Captain America',
                'difficulty': 'Hard',
                'duration': 45,
                'calories_estimate': 500,
                'activity_type': 'CrossFit'
            },
            {
                'name': 'Speedster Sprint',
                'description': 'Lightning-fast interval training inspired by The Flash',
                'difficulty': 'Hard',
                'duration': 30,
                'calories_estimate': 400,
                'activity_type': 'Running'
            },
            {
                'name': 'Warrior Yoga',
                'description': 'Flexibility and strength training fit for Wonder Woman',
                'difficulty': 'Medium',
                'duration': 60,
                'calories_estimate': 300,
                'activity_type': 'Yoga'
            },
            {
                'name': 'Hulk Smash Weights',
                'description': 'Heavy lifting program to build incredible strength',
                'difficulty': 'Hard',
                'duration': 50,
                'calories_estimate': 450,
                'activity_type': 'Weightlifting'
            },
            {
                'name': 'Atlantean Swim',
                'description': 'Intense swimming workout from the depths of Atlantis',
                'difficulty': 'Medium',
                'duration': 40,
                'calories_estimate': 350,
                'activity_type': 'Swimming'
            },
            {
                'name': 'Dark Knight Martial Arts',
                'description': 'Combat training routine from the Batcave',
                'difficulty': 'Hard',
                'duration': 55,
                'calories_estimate': 480,
                'activity_type': 'Boxing'
            },
            {
                'name': 'Asgardian Endurance',
                'description': 'Legendary endurance training from the halls of Asgard',
                'difficulty': 'Hard',
                'duration': 70,
                'calories_estimate': 600,
                'activity_type': 'CrossFit'
            },
            {
                'name': 'Kryptonian Power Cycle',
                'description': 'High-powered cycling workout with super strength',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_estimate': 400,
                'activity_type': 'Cycling'
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts_data)} workouts'))
        
        # Calculate and create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = []
        
        for hero in all_heroes:
            activities = Activity.objects.filter(user_id=str(hero._id))
            total_calories = sum(activity.calories_burned for activity in activities)
            total_duration = sum(activity.duration for activity in activities)
            
            leaderboard_data.append({
                'user_id': str(hero._id),
                'team_id': hero.team_id,
                'total_calories': total_calories,
                'total_duration': total_duration,
                'hero': hero
            })
        
        # Sort by total calories (descending) and assign ranks
        leaderboard_data.sort(key=lambda x: x['total_calories'], reverse=True)
        
        for rank, data in enumerate(leaderboard_data, start=1):
            Leaderboard.objects.create(
                user_id=data['user_id'],
                team_id=data['team_id'],
                total_calories=data['total_calories'],
                total_duration=data['total_duration'],
                rank=rank
            )
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_data)} leaderboard entries'))
        
        # Print summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        
        # Show top 3 on leaderboard
        self.stdout.write(self.style.SUCCESS('\n=== Top 3 Heroes ==='))
        top_heroes = Leaderboard.objects.all().order_by('rank')[:3]
        for entry in top_heroes:
            hero = User.objects.get(_id=ObjectId(entry.user_id))
            self.stdout.write(
                f'{entry.rank}. {hero.name} - {entry.total_calories} calories, {entry.total_duration} minutes'
            )
