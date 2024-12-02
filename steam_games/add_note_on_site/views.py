from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View

from add_note_on_site.forms import GameNoteForm
from database.models import Game
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
    success_url = reverse_lazy("a")
    form_class = GameNoteForm

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()

    #     form = self.get_form(form_class)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(self.request, 'Группа успешно добавлена.')
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
            
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object_list'] = Group.objects.all()
    #     return context

def game_autocomplete(request):
    if 'term' in request.GET:
        query = request.GET['term']
        games = Game.objects.filter(name__icontains=query)[:20]  # Ограничиваем до 10 результатов
        results = [{'id': game.id, 'label': game.name} for game in games]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)
