import json
import os
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../test_data.json'))
        with open(file_path) as f:
            data = json.load(f)

        # Populate users
        for user_data in data['users']:
            User.objects.get_or_create(email=user_data['email'], defaults={'name': user_data['name']})

        # Populate teams
        for team_data in data['teams']:
            members = User.objects.filter(email__in=team_data['members'])
            team, created = Team.objects.get_or_create(name=team_data['name'])
            team.members.set(members)

        # Populate activities
        for activity_data in data['activities']:
            user = User.objects.get(email=activity_data['user'])
            Activity.objects.get_or_create(user=user, description=activity_data['description'])

        # Populate leaderboard
        for leaderboard_data in data['leaderboard']:
            user = User.objects.get(email=leaderboard_data['user'])
            Leaderboard.objects.get_or_create(user=user, defaults={'score': leaderboard_data['score']})

        # Populate workouts
        for workout_data in data['workouts']:
            user = User.objects.get(email=workout_data['user'])
            Workout.objects.get_or_create(user=user, defaults={'details': workout_data['details']})

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))