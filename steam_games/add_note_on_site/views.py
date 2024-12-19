from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View

from add_note_on_site.forms import GameNoteForm
from database.models import Game
from my_auth.models import Profile
from .models import GameNote
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from add_note_on_site.models import GameNote


class GameNoteCreateView(CreateView):
    model = GameNote
    template_name = "add_note_on_site/add.html"
    success_url = reverse_lazy("add_note_on_site:add_note")
    form_class = GameNoteForm

    def form_valid(self, form):
        # Устанавливаем профиль текущего пользователя в поле `profile`
        form.instance.user_profile = Profile.objects.get(user=self.request.user)
        print(Profile.objects.get(user=self.request.user))
        return super().form_valid(form)


class GameNoteListView(ListView):
    model = GameNote
    paginate_by = 10
    template_name = "add_note_on_site/my_notes.html"

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        # Фильтруем по Profile, а не по User
        queryset = GameNote.objects.filter(user_profile=profile).order_by("-created_at")
        return queryset


def game_autocomplete(request):
    if 'term' in request.GET:
        query = request.GET['term']
        games = Game.objects.filter(name__icontains=query)[:20]  # Ограничиваем до 10 результатов
        results = [{'id': game.id, 'label': game.name} for game in games]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)
