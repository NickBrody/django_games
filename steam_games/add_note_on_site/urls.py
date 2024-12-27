from django.urls import path
from .views import GameNoteCreateView, GameNoteListView, GameNoteUpdateView, GameNoteDeleteView

app_name = 'add_note_on_site'

urlpatterns = [
    # другие пути
    path("add_note/",GameNoteCreateView.as_view(), name="add_note"),
    path("my_notes/",GameNoteListView.as_view(), name="my_notes"),
    path("my_notes/<int:pk>",GameNoteUpdateView.as_view(), name="update"),
    path("my_notes/delete/<int:pk>",GameNoteDeleteView.as_view(), name="delete"),

]
