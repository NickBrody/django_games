from django.urls import path
from .views import GameNoteCreateView

urlpatterns = [
    # другие пути
    path("a/",GameNoteCreateView.as_view(), name="a"),
]
