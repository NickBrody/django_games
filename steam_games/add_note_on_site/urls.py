from django.urls import include, path
from .views import GameNoteCreateView, GameNoteListView, GameNoteUpdateView, GameNoteDeleteView
from rest_framework import routers
from .views import GameNoteViewSet

app_name = 'add_note_on_site'

router = routers.DefaultRouter()
router.register(r'game-notes', GameNoteViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("add_note/",GameNoteCreateView.as_view(), name="add_note"),
    path("my_notes/",GameNoteListView.as_view(), name="my_notes"),
    path("my_notes/<int:pk>",GameNoteUpdateView.as_view(), name="update"),
    path("my_notes/delete/<int:pk>",GameNoteDeleteView.as_view(), name="delete"),

]
