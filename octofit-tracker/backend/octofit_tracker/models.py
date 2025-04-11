from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    # ...additional fields...

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)
    # ...additional fields...

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    # ...additional fields...

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    # ...additional fields...

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    # ...additional fields...