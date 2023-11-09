from django import forms

GAMES = [
    ("C", "COINS"),
    ("B", "CUBE"),
    ("N", "RANDOM_NUMBER"),
]

# структура формы для  выбора игры и выбора кол попыток
class GameForm(forms.Form):
    game = forms.ChoiceField(choices=GAMES)                 #поле для выбора игры
    attempts = forms.IntegerField(min_value=1, max_value=64) #поле для выбора кол попыток