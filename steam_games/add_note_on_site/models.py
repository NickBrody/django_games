from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class GameNote(models.Model):
    name = models.TextField()
    is_finished = models.BooleanField()
    want_to_play = models.BooleanField()
    score = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])
    hours = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
