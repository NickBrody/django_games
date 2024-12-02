from django.db import models


class Game(models.Model):
    app_id = models.BigIntegerField(unique=True, default=1)
    name = models.TextField(db_index=True)

    def __str__(self):
        return self.name
