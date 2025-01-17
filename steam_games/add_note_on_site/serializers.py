from rest_framework import serializers
from .models import GameNote

class GameNoteSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(source='user_profile.user.username')

    class Meta:
        model = GameNote
        fields = [
            "pk", 
            "name", 
            "is_finished", 
            "want_to_play", 
            "score", 
            "hours",
            "created_at",
            "user_profile",
        ]

