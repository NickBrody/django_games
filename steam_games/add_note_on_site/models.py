from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from my_auth.models import Profile


class GameNote(models.Model):
    name = models.TextField()
    is_finished = models.BooleanField()
    want_to_play = models.BooleanField()
    score = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    hours = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='game_notes', null=True)
    optional_notes = models.TextField(null=True)

    def __str__(self):
        return self.name
