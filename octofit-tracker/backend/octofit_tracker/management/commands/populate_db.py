from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import connection
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data using raw SQL to avoid unhashable errors
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM octofit_tracker_user;")
            cursor.execute("DELETE FROM octofit_tracker_team_members;")
            cursor.execute("DELETE FROM octofit_tracker_team;")
            cursor.execute("DELETE FROM octofit_tracker_activity;")
            cursor.execute("DELETE FROM octofit_tracker_leaderboard;")
            cursor.execute("DELETE FROM octofit_tracker_workout;")

        # Add test users without specifying IDs (MongoDB will generate ObjectIds automatically)
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', age=30)
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=25)

        # Add test teams and ensure members are added correctly
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Add test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-08')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-08')

        # Add test leaderboard entries
        Leaderboard.objects.create(user=user1, points=100)
        Leaderboard.objects.create(user=user2, points=150)

        # Add test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session', duration=60)
        Workout.objects.create(name='HIIT', description='High-intensity interval training', duration=30)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
