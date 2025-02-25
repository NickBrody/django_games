from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from add_note_on_site.models import GameNote
from add_note_on_site.forms import GameNoteForm
from database.models import Game
from my_auth.models import Profile
from .models import GameNote
from .serializers import GameNoteSerializer


class GameNoteViewSet(ModelViewSet):
    queryset = GameNote.objects.all().order_by("-created_at")
    serializer_class = GameNoteSerializer
    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]
    search_fields = ["name", "score"]
    ordering_fields = ["name", "score", "hours", "created_at"]
    permission_classes = [permissions.IsAdminUser]


class GameNoteCreateView(CreateView):
    model = GameNote
    template_name = "add_note_on_site/add.html"
    success_url = reverse_lazy("add_note_on_site:my_notes")
    form_class = GameNoteForm

    def form_valid(self, form):
        # Устанавливаем профиль текущего пользователя в поле `profile`
        form.instance.user_profile = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class GameNoteUpdateView(UpdateView):
    model = GameNote
    template_name = "add_note_on_site/update.html"
    success_url = reverse_lazy("add_note_on_site:my_notes")
    form_class = GameNoteForm


class GameNoteDeleteView(DeleteView):
    model = GameNote
    success_url = reverse_lazy("add_note_on_site:my_notes")


class GameNoteListView(ListView):
    model = GameNote
    paginate_by = 10
    template_name = "add_note_on_site/my_notes.html"

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        # Фильтруем по Profile, а не по User
        queryset = GameNote.objects.filter(user_profile=profile).select_related('user_profile').order_by("-id")
        return queryset


def game_autocomplete(request):
    if 'term' in request.GET:
        query = request.GET['term']
        games = Game.objects.filter(name__icontains=query)[:20]  # Ограничиваем до 10 результатов
        results = [{'id': game.id, 'label': game.name} for game in games]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)
