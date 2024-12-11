from django.urls import path
from .views import GameNoteCreateView, GameNoteListView

app_name = 'add_note_on_site'

urlpatterns = [
    # другие пути
    path("add_note/",GameNoteCreateView.as_view(), name="add_note"),
    path("my_notes/",GameNoteListView.as_view(), name="my_notes"),
]
