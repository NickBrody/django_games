import json
from django.core.management.base import BaseCommand
from database.models import Game  # Замените myapp на имя вашего приложения

class Command(BaseCommand):
    help = "Import apps from JSON file"

    def handle(self, *args, **kwargs):
        with open('steam.json', 'r', encoding='utf-8') as file:  # Замените apps.json на путь к вашему файлу
            data = json.load(file)
            apps = data.get("applist", {}).get("apps", [])
            
            for app in apps:
                Game.objects.update_or_create(app_id=app["appid"], defaults={"name": app["name"]})
            
        self.stdout.write(self.style.SUCCESS("Apps imported successfully"))
