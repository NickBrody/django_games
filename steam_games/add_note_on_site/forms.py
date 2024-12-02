from django import forms
from add_note_on_site.models import GameNote


class GameNoteForm(forms.ModelForm):

    # name = forms.CharField(
    #     label="Введите название игры",
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Введите название игры",
    #             "class": "form-control",
    #         }
    #     ),
    # )
    
    name = forms.CharField(
            label="Введите название игры",
            required=True,
            widget=forms.TextInput(
                attrs={
                    "placeholder": "Введите название игры",
                    "class": "form-control",
                    "id": "game-name",  # ID для поля, который будет использован в JS
                }
            ),
        )

    is_finished = forms.BooleanField(
        label="Прошёл!",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

    want_to_play = forms.BooleanField(
        label="Буду играть",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )

    score = forms.IntegerField(
        label="Ваша оценка игре до 100",
        required=False,
        widget=forms.NumberInput(),
        min_value=0,
        max_value=100
    )

    hours = forms.IntegerField(
        label="Сколько часов ушло на прохождение?",
        required=False,
        widget=forms.NumberInput(),
        min_value=0,

    )

    class Meta:
        model = GameNote
        fields = ["name", "is_finished", "want_to_play", "score", "hours"]