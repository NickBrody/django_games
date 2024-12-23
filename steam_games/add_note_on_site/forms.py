from django import forms
from add_note_on_site.models import GameNote


class GameNoteForm(forms.ModelForm):
    
    name = forms.CharField(
        label="Введите название игры*",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите название игры",
                "class": "form-control mb-3",
                'style': 'width: 100%; height: 45px; font-size: 18px;',
                "id": "game-name",
            }
        ),
    )

    is_finished = forms.BooleanField(
        label="Игру уже прошёл!",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input me-2"}),
    )

    want_to_play = forms.BooleanField(
        label="Буду играть или играю сейчас",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input me-2"}),
    )

    score = forms.IntegerField(
        label="Ваша оценка игре до 100",
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-3',
            'min': 0,
            'max': 100,
            'style': 'width: 30%; height: 40px; font-size: 18px;'
        }),
        min_value=0,
        max_value=100
    )

    hours = forms.IntegerField(
        label="Сколько часов ушло на прохождение?",
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-3',
            'style': 'width: 30%; height: 40px; font-size: 18px;'
        }),
        min_value=0,
    )

    optional_notes = forms.CharField(
        label="Дополнительные заметки",
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Введите ваши заметки здесь",
                "class": "form-control mb-3",
                'style': 'height: 150px; width: 100%; font-size: 16px; resize: vertical;'
            }
        )
    )

    class Meta:
        model = GameNote
        fields = ["name", "is_finished", "want_to_play", "score", "hours", "optional_notes"]
